from django.urls import path

from . import main

urlpatterns = [
    path("add", main.add),
    path("update", main.update),
    path("delete", main.delete),
    path("basic-get", main.basic_get),
    path("detailed-get", main.detailed_get),
]