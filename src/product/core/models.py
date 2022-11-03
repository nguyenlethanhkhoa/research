from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    modified_at = models.DateTimeField(blank=False, null=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True
