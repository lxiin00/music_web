from django.urls import path
from .views import playView, downloadView


urlpatterns = [
    path('<int:song_id>.html', playView, name='play'),
    path('download/<int:song_id>/<str:song_name>.html', downloadView, name='download'),
]