from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class ProductViewSet(APIView):

    # queryset = Article.objects.select_related('author', 'author__user')

    def get(self, request):
        print("================")
        print("Has hecho un GET")
        print("================")
        return Response("Has hecho un get", status=status.HTTP_200_OK)