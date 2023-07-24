from django.contrib import admin
from django.urls import path, include
from .views import search_api

urlpatterns = [
    path('', search_api)
]