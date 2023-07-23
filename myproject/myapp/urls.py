# myapp/urls.py
print("Carregando myapp/urls.py...")

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.search_api, name='search_api'),

]
