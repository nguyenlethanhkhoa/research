from django.db import models

class Product(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    tags = models.ManyToManyField(
        'tag.Tag', related_name='products'
    )
    categories = models.ManyToManyField(
        'category.Category', on_delete=models.CASCADE, related_name='products'
    )
    property_names = models.ManyToManyField(
        'product.PropertyName',
        on_delete=models.CASCADE
    )
    property_values = models.ManyToField(
        'product.PropertyValue',
        on_delete=models.CASCADE
    )

class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.IntegerField(default=0)

    property_names = models.ManyToManyField(
        'product.PropertyName',
        on_delete=models.CASCADE
    )
    property_values = models.ManyToManyField(
        'product.PropertyValue',
        on_delete=models.CASCADE
    )

class PropertyName(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    required = models.BooleanField(default=False)
    selectable = models.BooleanField(default=False)

class PropertyValue(models.Model):
    property_id = models.BigIntegerField()
    product_id = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, null=True
    )
    product_variant_id = models.ForeignKey(
        'product.ProductVariant', on_delete=models.CASCADE, null=True
    )
    value = models.TextField()