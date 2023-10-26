from django.urls import path

from . import main

urlpatterns = [
    path("add/", main.add, name="add"),
]