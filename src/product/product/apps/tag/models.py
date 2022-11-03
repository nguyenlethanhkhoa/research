from django.db import models

from product.apps.core.models import BaseModel

class Tag(BaseModel):
    title = models.CharField(max_length=70)
    description = models.TextField(null=True)