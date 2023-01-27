from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("lucas", views.lucas, name="lucas"),
    path("david", views.david, name="david")
]