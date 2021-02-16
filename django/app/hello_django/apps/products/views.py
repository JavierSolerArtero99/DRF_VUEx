from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status, mixins
from rest_framework.response import Response
# from rest_framework.permissions import (IsAuthenticatedOrReadOnly)

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(mixins.CreateModelMixin, 
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin):

    # permissions_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer

    results = Product.objects.all()
    serializer = ProductSerializer

    def get_queryset(self):
        return self.queryset

    # def get(self, request):
    #     serializedData = ProductSerializer(self.results, many=True)
    #     return Response({'ProductsList': serializedData.data}, status=status.HTTP_200_OK)

    def create(self, request):

        serializer_context = {
            'author': request.user.profile,
            'request': request
        }

        serializer_data = request.data.get('product', {})

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, satus=status.HTTP_201_CREATED)

        # newProduct = request.data.get('product', {})
        # serializer = ProductSerializer(data=newProduct)
        # serializer.is_valid(raise_exception=True)
        # # serializer.author = 
        # print("NUEVO PRODUCTO")
        # print(serializer)
        # serializer.save()

        # return Response({"CREATE": "DONE"}, status=status.HTTP_201_CREATED)
