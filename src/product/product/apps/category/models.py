from django.db import models

from product.apps.core.models import BaseModel

class Category(BaseModel):
    parent_id = models.BigIntegerField()
    title = models.CharField(max_length=70)
    description = models.TextField()

    class Meta:
        db_table = 'category'