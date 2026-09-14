from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("add/", views.add_birthday, name="add"),
    path("delete/<int:id>/", views.delete_birthday, name="delete"),
]
