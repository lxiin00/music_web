from django.urls import path
from .views import commentView


urlpatterns =[
    path('<int:song_id>.html', commentView, name='comment'),
]