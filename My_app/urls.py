from django.urls import path, re_path
from . import views

urlspatterns = [
    path("", views.home, name="home")
  
]