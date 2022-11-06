from django.urls import path

from views import CategoryViewSet

app_name = 'categories'
urlpatterns = [
    path('', CategoryViewSet),
]
