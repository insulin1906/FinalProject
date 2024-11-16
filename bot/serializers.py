from rest_framework import serializers
from .models import ProductQuery


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuery
        fields = ['id', 'name', 'description', 'price', 'category']

