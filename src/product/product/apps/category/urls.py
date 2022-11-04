from django.urls impot path

from . import views

app_name = 'categories'
urlpatterns = [
    # ex: /polls/
    path('', views.get_items, name='index'),
]