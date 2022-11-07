from django.db import models

from product.apps.core.models import BaseModel


class CategoryManager(models.Manager):
    pass


class Category(BaseModel):
    parent_id = models.BigIntegerField(null=True)
    title = models.CharField(max_length=70)
    description = models.TextField(null=True)

    objects = CategoryManager()

    class Meta:
        db_table = 'category'

    @classmethod
    def create(cls, title, parent_id=None, description=None):
        category = cls(
            title=title,
            parent_id=parent_id,
            description=description
        )
        return category
