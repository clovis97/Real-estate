from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('dashboard', views.dashboard, name='dashboard'),
] 