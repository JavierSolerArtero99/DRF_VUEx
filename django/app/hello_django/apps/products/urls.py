# from django.conf.urls import include, url

# from rest_framework.routers import DefaultRouter

from .views import (
    ProductViewSet
)

# # router = DefaultRouter(trailing_slash=False)
# # router.register(r'products', ProductViewSet)

# urlpatterns = [
#     # url(r'^', include(router.urls)),
#     url(r'/products/?$', ProductViewSet.as_view()),
# ]
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^products/?$', csrf_exempt(ProductViewSet)),
]
