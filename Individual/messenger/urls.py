from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path
urlpatterns = [
    path('', views.Login, name='login'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('home/', views.Home, name='home'),
    path('post/', views.Post, name='post'),
    path('messages/', views.Messages, name='messages'),


]
