
from django.urls import path

from . import views

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    path('', views.index),
]
