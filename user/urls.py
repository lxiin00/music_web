from django.urls import path
from .views import loginView, logoutView


urlpatterns = [
    path('login.html', loginView, name='login'),
    path('logout.html', logoutView, name='logout'),
]