from rest_framework import serializers
from models import Product

class ProductSerializer(serializers.ModelsSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'description', 'stock', 'image']