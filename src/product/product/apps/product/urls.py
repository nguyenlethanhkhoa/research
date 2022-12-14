from rest_framework.routers import DefaultRouter

from .views import ProductViewSet


app_name = 'categories'
router = DefaultRouter(trailing_slash=False)
router.register('products', ProductViewSet)
router.register('products/<int:product_id>/variants', ProductViewSet)
