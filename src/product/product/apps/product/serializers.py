from rest_framework import serializers

from .models import Product, ProductVariant, PropertyName, PropertyValue
from ..category.models import Category
from ..category.serializers import CategorySerializer
from ..tag.models import Tag
from ..tag.serializers import TagSerializer


class PropertyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyName
        fields = '__all__'


class PropertyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyValue
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    property_names = PropertyNameSerializer(many=True)
    property_values = PropertyValueSerializer(many=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)
    properties = PropertyNameSerializer(many=True)

    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    category_ids = serializers.StringRelatedField(many=True, write_only=True)
    tag_ids = serializers.StringRelatedField(many=True, write_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        properties = validated_data.get('properties')
        category_ids = validated_data.get('category_ids')
        tag_ids = validated_data.get('tag_ids')

        product = Product.objects.create(**validated_data)

        product.categories = Category.objects.filter(id__in=category_ids).all()
        product.tags = Tag.objects.filter(id__in=tag_ids).all()

        for prop in properties:
            item = PropertyName.objects.create(**prop)
            item_value = PropertyValue.objects.create(
                property_id=item.id,
                value=prop.get('value'),
                object_type=product
            )

        product.save()
