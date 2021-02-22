from rest_framework import serializers

from .models import Product
from ..profiles.serializers import ProfileSerializer

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    title = serializers.CharField(required=True)
    image = serializers.CharField(required=False)
    price = serializers.FloatField(max_value=None, min_value=None, required=False)
    description = serializers.CharField(required=True)
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'slug',
            'title',
            'image',
            'price',
            'description',
            'author'
        )
     
    def create(self, validated_data):
        author = self.context.get('author', None)

        product = Product.objects.create(author=author, **validated_data)

        return product
