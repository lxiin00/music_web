from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('rankingList', include('ranking.urls')),
    path('play/', include('play.urls')),
    path('comment/', include('comment.urls')),
    path('search/', include('search.urls')),
    # path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
]
