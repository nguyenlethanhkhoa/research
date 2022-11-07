from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    modified_at = models.DateTimeField(blank=False, null=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    def soft_delete(self):
        self.deleted_at = datetime.now()

    class Meta:
        abstract = True

