from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(nullable=False, auto_now_add=True)
    modified_at = models.DateTimeField(nullable=False, auto_now=True)
    deleted_at = models.DateTimeField(nullable=True)

class Category(BaseModel):
    parent_id = models.BigIntegerField()
    title = models.CharField(max_length=70)
    description = models.TextField()

class Tag(BaseModel):
    title = models.CharField(max_length=70)
    description = models.TextField()

class Product(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    property_names = models.ManyToManyField(PropertyName)
    property_values = models.ManyToManyField(PropertyValue)

class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    qty = models.IntegerField()

    property_names = models.ManyToManyField(PropertyName)
    property_values = models.ManyToManyField(PropertyValue)

class PropertyName(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    required = models.BooleanField(default=False)
    selectable = models.BooleanField(default=False)

class PropertyValue(models.Model):
    property_id = models.BigIntegerField()
    value = models.TextField()