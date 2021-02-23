from django.db import models


# class TimestampedModel(models.Model):
#     # A timestamp representing when this object was created.
#     created_at = models.DateTimeField(auto_now_add=True)

#     # A timestamp reprensenting when this object was last updated.
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
#         # By default, any model that inherits from `TimestampedModel` should
#         # be ordered in reverse-chronological order. We can override this on a
#         # per-model basis as needed, but reverse-chronological is a good
#         # default ordering for most models.
#         ordering = ['-created_at', '-updated_at']

from ..profiles.models import Profile


class Product(models.Model):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)
    image = models.TextField(default=None)

    description = models.TextField()
    body = models.TextField()
    price = models.FloatField(default=0)

    author = models.ForeignKey(
        'profiles.Profile', related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Like(models.Model):
    likes = models.IntegerField(default=0)

    likeAuthor = models.ForeignKey(
        'profiles.Profile', related_name='likeAuthor', on_delete=models.CASCADE)

    likeProduct = models.ForeignKey(
        'products.Product', related_name='likeProduct', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.likes}"


class Comment(models.Model):
    message = models.CharField(default="",  max_length=255)

    commentAuthor = models.ForeignKey(
        'profiles.Profile', related_name='commentAuthor', on_delete=models.CASCADE)

    commentProduct = models.ForeignKey(
        'products.Product', related_name='commentProduct', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"{self.likes}"
