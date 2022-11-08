from .models import Tag
from .serializers import TagSerializer
from ..core.views import BaseViewSet


class TagViewSet(BaseViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        parent_id = self.request.query_params.get('parent_id')

        query = self.queryset
        if title:
            query = query.filter(title=title)
        if parent_id:
            query = query.filter(parent_id=parent_id)

        return query

