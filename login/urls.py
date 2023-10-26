from django.urls import path

from . import main

urlpatterns = [
    path("csrf/", main.get_csrf_token, name="csrf"),
]