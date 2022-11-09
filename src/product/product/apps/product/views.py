from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer, ProductVariantSerializer
from ..core.views import BaseViewSet


class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductVariantViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductVariantSerializer

