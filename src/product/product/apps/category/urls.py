from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet


app_name = 'categories'
router = DefaultRouter()
router.register('', 'categories', CategoryViewSet)
