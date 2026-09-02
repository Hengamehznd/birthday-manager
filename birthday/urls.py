from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("add/<str:name>/<str:birthday>/", views.add_birthday, name="add"),
]
