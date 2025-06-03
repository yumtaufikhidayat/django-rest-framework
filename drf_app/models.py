import uuid

from django.db import models

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=30)
    description = models.TextField()
    shop = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.CharField(max_length=10)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=False)
    picture = models.URLField(max_length=500)