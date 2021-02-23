# from django.conf.urls import include, url

# from rest_framework.routers import DefaultRouter

from .views import (
    ProductViewSet,
    LikeProductAPIView,
    CommentAPIView,
    CommentsDestroyAPIView,
    BuyProductAPIView,
    ProductsByUser
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
    url(r'^products/(?P<product_slug>[-\w]+)/comments/?$',
        CommentAPIView.as_view()),
    url(r'^products/(?P<product_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',
        CommentsDestroyAPIView.as_view()),
    url(r'^products/buy/(?P<product_slug>[-\w]+)/?$',
        BuyProductAPIView.as_view()),
    url(r'^productsByUser/?$',
        ProductsByUser.as_view()),
]
# urlpatterns = [
#     url(r'^products/?$', csrf_exempt(ProductViewSet)),
# ]
