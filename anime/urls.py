from django.contrib import admin
from django.urls import path, include
from anime import views


urlpatterns = [
    path('', views.index, name='index'),
    path('anime/<slug:anime_slug>/', views.watch_anime, name='watch_anime'),
    path('category/', views.page_category, name='category'),
    path('category/<slug:category_slug>/', views.page_category, name='category_by_slug'),
    path('category/<int:catrgory_int>/', views.page_category, name='category_by_int'),
    path('add_comment/<slug:anime_slug>/', views.add_comment, name='add_comment'),
]