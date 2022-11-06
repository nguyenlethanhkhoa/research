from rest_framework import routers

from .views import CategoryViewSet

app_name = 'categories'
router = routers.DefaultRouter()
router.register('', CategoryViewSet)
