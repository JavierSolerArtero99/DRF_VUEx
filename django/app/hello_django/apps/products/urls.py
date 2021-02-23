# from django.conf.urls import include, url

# from rest_framework.routers import DefaultRouter

from .views import (
    ProductViewSet,
    LikeProductAPIView
)

# # router = DefaultRouter(trailing_slash=False)
# # router.register(r'products', ProductViewSet)

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

app_name = 'products'

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^products/(?P<product_slug>[-\w]+)/like/?$',
        LikeProductAPIView.as_view()),
]
# urlpatterns = [
#     url(r'^products/?$', csrf_exempt(ProductViewSet)),
# ]
