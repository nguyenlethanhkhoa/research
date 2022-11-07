from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet


app_name = 'categories'
router = DefaultRouter(trailing_slash=False)
router.register('categories', CategoryViewSet)
