"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .apps.tag.urls import router as tag_router
from .apps.product.urls import router as product_router
from .apps.category.urls import router as category_router

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
   path('product/', include(tag_router.urls)),
   path('product/', include(product_router.urls)),
   path('product/', include(category_router.urls)),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
