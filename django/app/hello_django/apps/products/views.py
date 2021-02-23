from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated)

from .models import Product, Like
from .serializers import ProductSerializer, LikeSerializer
from ..profiles.serializers import ProfileSerializer


class ProductViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        viewsets.GenericViewSet):

    lookup_field = 'slug'
    # permissions_classes = (IsAuthenticatedOrReadOnly,)
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

        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, slug):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

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

    def destroy(self, request, slug):
        try:
            product = self.queryset.get(slug=slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug does not exist.')

        product.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class LikeProductAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    # renderer_classes = (ArticleJSONRenderer,)
    serializer_class = LikeSerializer
    queryset = Like.objects.select_related(
        'likeAuthor', 'likeAuthor', 'likeProduct', 'likeProduct', )

    def get_queryset(self):
        queryset = self.queryset

        # author = self.request.query_params.get('author', None)
        # if author is not None:
        #     queryset = queryset.filter(author__user__username=author)
        return queryset


    def delete(self, request, product_slug=None):
        profile = self.request.user.profile
        # serializer_context = {'request': request}

        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug was not found.')

        # try:
        #     like = Like.objects.get(likeAuthor=profile)
        # except Like.DoesNotExist:
        #     raise NotFound('LIKE not found.')

        # profile.unfavorite(article)

        # serializer = self.serializer_class(article, context=serializer_context)

        return Response({"product": "Like deleted"}, status=status.HTTP_200_OK)

    # Obtiene si el usuario le ha dado like a ese producto
    def get(self, request, product_slug=None):
        profile = self.request.user.profile

        # Finding product
        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug was not found.')

        # Finding like
        try:
            like = Like.objects.get(likeAuthor=profile, likeProduct=product)
            serializer = self.serializer_class(like)
        except Like.DoesNotExist:
            raise NotFound('LIKE not found.')

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, product_slug=None):
        profile = self.request.user.profile

        # Finding product
        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug was not found.')

        # Finding like
        try:
            like = Like.objects.get(likeAuthor=profile, likeProduct=product)
            print(like)
            serializer = self.serializer_class(like)
        except Like.DoesNotExist:
            print("NOOO")
            # raise NotFound('LIKE not found.')

        return Response({"serializer.data": "fd"}, status=status.HTTP_201_CREATED)
