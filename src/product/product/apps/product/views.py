from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer
from ..core.views import BaseViewSet


class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        parent_id = self.request.query_params.get('parent_id')

        query = self.queryset
        if title:
            query = query.filter(title=title)
        if parent_id:
            query = query.filter(parent_id=parent_id)

        return query

