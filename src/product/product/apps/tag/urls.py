from rest_framework.routers import DefaultRouter

from .views import TagViewSet


app_name = 'categories'
router = DefaultRouter(trailing_slash=False)
router.register('tags', TagViewSet)
