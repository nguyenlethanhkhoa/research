from .views import CategoryViewSet
from product.apps.core.routers import CustomRouter

app_name = 'categories'
router = CustomRouter()
router.register('', CategoryViewSet)
