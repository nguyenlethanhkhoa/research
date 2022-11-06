from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        query = Category.objects.all()
        title = request.query_params.get('title')
        parent_id = request.query_params.get('parent_id')

        if title:
            query = query.filter(title=title)
        if parent_id:
            query = query.filter(parent_id=parent_id)
        return query

    def create(self, request):
        item = Category.objects.create(
            title=request.data.get('title'),
            parent_id=request.data.get('parent_id'),
            description=request.data.get('description')
        )

        return item
