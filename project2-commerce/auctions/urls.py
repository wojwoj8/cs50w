from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create_listing, name="createlisting"),
    path("listing/<int:listing_id>", views.listing, name="list"),
    path("closed/listing/<int:listing_id>", views.closed, name="close"),
    path("tmp/listing/<int:listing_id>", views.comment, name="comment"),
    path("tmpp/listing/<int:listing_id>", views.watch, name="watch"),
    path("watched", views.listwatch, name="listwatch"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category>", views.categorylist, name="categorylist"),
]
