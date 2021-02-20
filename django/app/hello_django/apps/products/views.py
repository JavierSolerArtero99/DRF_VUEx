from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)

from .models import Product
from .serializers import ProductSerializer
from ..profiles.serializers import ProfileSerializer

class ProductViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):

    permissions_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related('author', 'author__user')
    serializer = ProductSerializer
    userSerializer = ProfileSerializer

    def get_queryset(self):
        queryset = self.queryset

        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author__user__username=author)
        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        # return self.get_paginated_response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request):

        serializer_context = {
            'author': request.user.profile,
            'request': request
        }


        serializer_data = request.data.get('product', {})
        # author_serialized = request.data.get('product.user', {})
        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )   
        serializer.is_valid(raise_exception=True)
        # author = serializer.data.author
        # print(serializer.data.author)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
