from django.urls import path
from .views import loginView, logoutView, homeView


urlpatterns = [
    path('login.html', loginView, name='login'),
    path('logout.html', logoutView, name='logout'),
    path('home/<int:page>.html', homeView, name='home'),
]