from django.urls import path
from .views import searchView


urlpatterns = [
    path('<int:page>.html', searchView, name='search'),
]