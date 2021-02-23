from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status, mixins, viewsets, generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated)

from .models import Product, Like, Comment
from .serializers import ProductSerializer, LikeSerializer, CommentSerializer
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
        page = self.paginate_queryset(self.get_queryset().order_by('id'))

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

    def update(self, request, slug):
        serializer_context = {
            'author': request.user.profile,
            'request': request
        }

        try:
            serializer_instance = self.queryset.get(slug=slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug does not exist.')

        serializer_data = request.data.get('product', {})

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, slug):
        try:
            product = self.queryset.get(slug=slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug does not exist.')

        product.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class LikeProductAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

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

        return Response(serializer.data, status=status.HTTP_200_OK)

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
            return Response({"details": "Product already Liked"}, status=status.HTTP_208_ALREADY_REPORTED)
        except Like.DoesNotExist:
            newLike = Like(likeAuthor=profile, likeProduct=product)
            newLike.save()

        return Response({"details": "Successfull liked"}, status=status.HTTP_201_CREATED)

    def delete(self, request, product_slug=None):
        profile = self.request.user.profile

        # Finding product
        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug was not found.')

        # Finding like
        try:
            like = Like.objects.get(likeAuthor=profile, likeProduct=product)
            like.delete()
        except Like.DoesNotExist:
            raise NotFound('A product with this slug was not found.')

        return Response({"details": "Successfull deleted"}, status=status.HTTP_201_CREATED)


class CommentAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    # Obtiene los comentarios del producto que se ha pasado por slug
    def get(self, request, product_slug=None):
        profile = self.request.user.profile

        # Finding product
        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug was not found.')

        # Finding comments
        try:
            comments = Comment.objects.filter(commentProduct=product)
            serializer = self.serializer_class(comments, many=True)
        except Like.DoesNotExist:
            raise NotFound('Comments not founds.')

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, product_slug=None):
        profile = self.request.user.profile

        # Finding product
        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug was not found.')

        serializer_data = request.data.get('comment', {})
        # author_serialized = request.data.get('product.user', {})
        serializer = self.serializer_class(
            data=serializer_data
        )
        serializer.is_valid(raise_exception=True)

        # print(serializer.data.get('message'))
        newComment = Comment(commentAuthor=profile, commentProduct=product,
                             message=serializer.data.get('message'))
        newComment.save()

        return Response({"details": "Comment created"}, status=status.HTTP_201_CREATED)


class CommentsDestroyAPIView(generics.DestroyAPIView):
    lookup_url_kwarg = 'comment_pk'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()

    def destroy(self, request, product_slug=None, comment_pk=None):
        try:
            comment = Comment.objects.get(pk=comment_pk)
        except Comment.DoesNotExist:
            raise NotFound('A comment with this ID does not exist.')

        comment.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class BuyProductAPIView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProfileSerializer
            
    def post(self, request, product_slug=None, comment_pk=None):
        profile = self.request.user.profile

        # Finding product
        try:
            product = Product.objects.get(slug=product_slug)
        except Product.DoesNotExist:
            raise NotFound('A product with this slug was not found.')

        profile.buyProduct()
        profile.save()

        return Response({"Success": "Product buyed (karma updated)"}, status=status.HTTP_204_NO_CONTENT)
