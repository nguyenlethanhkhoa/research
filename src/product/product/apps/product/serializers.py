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

    class Meta:
        model = ProductVariant
        exclude = ['property_names']


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, write_only=True)
    properties = PropertySerializer(many=True, write_only=True)

    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    category_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )
    tag_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )

    class Meta:
        model = Product
        exclude = ['property_names']

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
                selectable=prop.get('selectable')
            )
            property_names.append(item)
            item_value = PropertyValue.objects.create(
                property_id=item.id,
                value=prop.get('value'),
                object_type=product
            )

        product.property_names.set(property_names)

        return product

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['properties'] = PropertySerializer(instance.property_names.all(), many=True).data.items,
        return ret

