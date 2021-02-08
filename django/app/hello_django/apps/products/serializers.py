from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=True)
    body = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = (
            'slug',
            'title',
            'description',
            'body'
        )