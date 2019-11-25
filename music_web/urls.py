from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views import static
from django.conf import settings


urlpatterns = [
    path('', include('index.urls')),
    path('rankingList', include('ranking.urls')),
    path('play/', include('play.urls')),
    path('comment/', include('comment.urls')),
    path('search/', include('search.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    # 设置项目上线的静态资源路径
    url('^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]


from index.views import page_not_found

handler404 = page_not_found
handler500 = page_not_found