from django.urls import path

from . import main

urlpatterns = [
    path("add", main.add),
    path("update", main.update),
    path("delete", main.delete),
    path("get", main.get),
    path("update-profile", main.update_profile)
]