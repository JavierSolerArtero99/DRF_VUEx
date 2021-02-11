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


class Product(models.Model):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)

    description = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
