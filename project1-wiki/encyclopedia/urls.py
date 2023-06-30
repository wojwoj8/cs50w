from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.title, name="name"),
    path("search", views.searc, name="search"),
    path("addpage", views.add, name="addpage"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("wiki", views.random, name="random")
    
]
