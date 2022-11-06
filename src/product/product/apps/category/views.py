from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer

class CategoryListView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        query = Category.objects.all()
        if self.request.query_params.title:
            query = query.filter(
                title=self.request.query_params.title
            )
        if self.request.query_params.parent_id:
            query = query.filter(
                parent_id=self.request.query_params.parent_id
            )
        return query

    def perform_create(self, serializer):
        serializer.save(
            title=self.request.data.title,
            parent_id=self.request.data.parent_id
        )
