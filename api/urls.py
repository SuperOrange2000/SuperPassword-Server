from django.urls import path

from . import main

urlpatterns = [
    path("add", main.add),
    path("update", main.update),
    path("delete", main.delete),
    path("quick-get-data", main.quick_get),
    path("get-data", main.get),
    path("update-profile", main.update_profile)
]