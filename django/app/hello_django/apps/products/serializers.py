from rest_framework import serializers

from .models import Product
from ..profiles.serializers import ProfileSerializer

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    title = serializers.CharField(required=True)
    image = serializers.CharField(required=False)
    price = serializers.FloatField(max_value=None, min_value=None, required=False)
    description = serializers.CharField(required=True)
    author = ProfileSerializer(required=False)

    class Meta:
        model = Product
        fields = (
            'slug',
            'title',
            'image',
            'price',
            'description',
            'author'
        )