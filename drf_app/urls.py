from django.urls import path
from drf_app import views

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-create'),
    path('products/<uuid:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]