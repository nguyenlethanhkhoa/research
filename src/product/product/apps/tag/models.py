from django.db import models

from product.apps.core.models import BaseModel, BaseManager


class TagManager(BaseManager):
    pass


class Tag(BaseModel):
    title = models.CharField(max_length=70)
    description = models.TextField(null=True)

    objects = TagManager()

    class Meta:
        db_table = 'tag'
