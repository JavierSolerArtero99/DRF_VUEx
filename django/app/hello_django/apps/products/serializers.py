from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
