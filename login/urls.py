from django.urls import path

from . import main

urlpatterns = [
    path("csrf/", main.get_csrf_token, name="csrf"),
    path("sign-up/", main.sign_up, name="sign up"),
    path("login/", main.login, name="login"),
]