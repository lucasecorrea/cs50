from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("lucas", views.lucas, name="lucas")
]