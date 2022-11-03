from django.db import models

class Tag(BaseModel):
    title = models.CharField(max_length=70)
    description = models.TextField(null=True)