from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        title = request.query_params.get('title')
        parent_id = request.query_params.get('parent_id')

        query = self.queryset
        if title:
            query = query.filter(title=title)
        if parent_id:
            query = query.filter(parent_id=parent_id)

        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)

    def create(self, request):
        item = Category.objects.create(
            title=request.data.get('title'),
            parent_id=request.data.get('parent_id'),
            description=request.data.get('description')
        )

        item.save()
        serializer = self.serializer_class(item)
        return Response(serializer.data)
