from django.contrib import admin
from django.urls import path, include
from anime import views


urlpatterns = [
    path('', views.index, name='index'),
    path('anime/<slug:anime_slug>/', views.watch_anime, name='watch_anime')
]