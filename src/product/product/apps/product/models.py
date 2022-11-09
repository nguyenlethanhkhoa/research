from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from product.apps.core.models import BaseModel, BaseManager


class ProductManager(BaseManager):
    pass


class ProductVariantManager(BaseManager):
    pass


class PropertyNameManager(BaseManager):
    pass


class PropertyValueManager(BaseManager):
    pass


class Product(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    tags = models.ManyToManyField('tag.Tag', related_name='products')
    categories = models.ManyToManyField('category.Category', related_name='products')
    property_names = models.ManyToManyField('product.PropertyName')

    objects = ProductManager()

    class Meta:
        db_table = 'product'


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.IntegerField(default=0)

    property_names = models.ManyToManyField('product.PropertyName')

    objects = ProductVariantManager()

    class Meta:
        db_table = 'product_variant'


class PropertyName(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    required = models.BooleanField(default=False)
    selectable = models.BooleanField(default=False)

    objects = PropertyNameManager()

    class Meta:
        db_table = 'property_name'


class PropertyValue(models.Model):
    property_id = models.BigIntegerField()
    object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    object_content = GenericForeignKey('object_type', 'object_id')
    value = models.TextField()

    objects = PropertyValueManager()

    class Meta:
        db_table = 'property_value'
