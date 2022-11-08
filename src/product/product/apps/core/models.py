from datetime import datetime

from django.db import models


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    modified_at = models.DateTimeField(blank=False, null=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()

    class Meta:
        abstract = True

