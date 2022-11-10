from rest_framework import serializers

from .models import Product, ProductVariant, PropertyName, PropertyValue
from ..category.models import Category
from ..category.serializers import CategorySerializer
from ..tag.models import Tag
from ..tag.serializers import TagSerializer


class PropertySerializer(serializers.ModelSerializer):

    value = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PropertyName
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)
    property_names = PropertySerializer(many=True, required=False)

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)
    properties = PropertySerializer(many=True, read_only=True)
    property_names = PropertySerializer(many=True, required=False)

    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    category_ids = serializers.StringRelatedField(many=True)
    tag_ids = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        properties = validated_data.get('properties', [])
        category_ids = validated_data.get('category_ids', [])
        tag_ids = validated_data.get('tag_ids', [])

        product = Product.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description')
        )

        product.categories.set(Category.objects.filter(id__in=category_ids).all())
        product.tags.set(Tag.objects.filter(id__in=tag_ids).all())

        property_names = []
        for prop in properties:
            item = PropertyName.objects.create(
                title=prop.get('title'),
                type=prop.get('type'),
                required=prop.get('required'),
                selectable=prop.get('selectable')
            )
            property_names.append(item)
            item_value = PropertyValue.objects.create(
                property_id=item.id,
                value=prop.get('value'),
                object_type=product
            )

        product.property_names.set(property_names)
        product.save()
