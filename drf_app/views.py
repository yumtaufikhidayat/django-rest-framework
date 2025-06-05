from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_app.models import Product
from drf_app.serializers import ProductSerializer

class ProductListCreateView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        location = request.query_params.get('location')

        products = Product.objects.filter(is_deleted=False)

        if name:
            products = products.filter(name__icontains=name)

        if location:
            products = products.filter(location__icontains=location)

        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response({
            "products": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)  # Hilangkan filter is_deleted=False
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.is_deleted = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

