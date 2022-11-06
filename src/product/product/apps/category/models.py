from django.db import models

from product.apps.core.models import BaseModel

class CategoryManager(models.Manager):
    def create(self, title, parent_id=None, description=None):
        category = self.create(
            title=title,
            parent_id=parent_id,
            description=description
        )
        return category

class Category(BaseModel):
    parent_id = models.BigIntegerField()
    title = models.CharField(max_length=70)
    description = models.TextField()

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
