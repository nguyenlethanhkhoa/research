from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        parent_id = self.request.query_params.get('parent_id')

        query = self.queryset
        if title:
            query = query.filter(title=title)
        if parent_id:
            query = query.filter(parent_id=parent_id)

        return query


