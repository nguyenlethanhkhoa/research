from django.db import models

from product.apps.core.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    tags = models.ManyToManyField(
        'tag.Tag', related_name='products'
    )
    categories = models.ManyToManyField(
        'category.Category', related_name='products'
    )

    class Meta:
        db_table = 'product'


class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.IntegerField(default=0)

    property_names = models.ManyToManyField(
        'product.PropertyName'
    )

    class Meta:
        db_table = 'product_variant'


class PropertyName(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    required = models.BooleanField(default=False)
    selectable = models.BooleanField(default=False)

    class Meta:
        db_table = 'property_name'


class PropertyValue(models.Model):
    property_id = models.BigIntegerField()
    product_id = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, null=True
    )
    product_variant_id = models.ForeignKey(
        'product.ProductVariant', on_delete=models.CASCADE, null=True
    )
    value = models.TextField()

    class Meta:
        db_table = 'property_value'