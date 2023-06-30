
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:uname>", views.profile_view, name="profile"),
    path("follows", views.follows, name="follows"),

    #API routes
    path("editPost/<int:post_id>", views.editPost, name="editPost"),
    path("likes/<int:post_id>", views.like, name="likes"),


]
