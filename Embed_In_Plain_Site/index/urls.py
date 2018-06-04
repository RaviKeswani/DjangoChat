from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('index/', views.test, name='test'),


    path('',include('messenger.urls')),
]