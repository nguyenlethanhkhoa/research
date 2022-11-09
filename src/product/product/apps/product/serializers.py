from rest_framework import serializers

from .models import Product, ProductVariant, PropertyName, PropertyValue


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
    property_names = PropertyNameSerializer(many=True)
    property_values = PropertyValueSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

