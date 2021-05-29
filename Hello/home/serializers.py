from django.db import models
from rest_framework import fields, serializers


from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "price",
            "desc",
            "baby_age",
            "image"
        ]