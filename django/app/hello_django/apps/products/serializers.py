from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    slug = "producto"
    title = "producto"
    description = "producto"
    body = "producto"
