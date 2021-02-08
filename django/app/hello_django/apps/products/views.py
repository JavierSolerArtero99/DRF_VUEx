from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(APIView):

    results = Product.objects.all()
    serializer = ProductSerializer

    def get_queryset(self):
        return self.queryset

    def get(self, request):
        serializedData = ProductSerializer(self.results, many=True)
        return Response({'ProductsList': serializedData.data}, status=status.HTTP_200_OK)
