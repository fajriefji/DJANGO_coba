from django.urls import path
from .import views

urlpatterns = [
    path('Blog', views.Blog, name='Blog'),
]