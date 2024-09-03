from django.db import models
from utils.random import random_string_func
from utils.storage import HashStorage
from django.utils import timezone
from functools import partial
import os
from core.exceptions import TokenTimeoutError
from datetime import datetime, timedelta
from typing import Any, ClassVar

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    guid = models.CharField(max_length=36)

    nickname = models.CharField(max_length=32, default="orange", blank=True)
    password = models.BinaryField(max_length=32)
    account = models.CharField(max_length=32)
    salt = models.CharField(max_length=64, default=random_string_func)
    profile_pic = models.ImageField(upload_to="profile_pic", storage=HashStorage(), default="profile_pic/default.png", blank=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        indexes = [
            models.Index(fields=["guid"])
        ]

class TokenManager(models.Manager):
    timeout = 300
    def get(self, *args, **kwargs):
        token = super().get(*args, **kwargs)
        if self.check_timeout(token):
            token.active_time = datetime.now(token.active_time.tzinfo)
            token.save()
            return token
        else:
            return None

    def check_timeout(self, token:models.Model) -> list[Any]:
        if datetime.now(token.active_time.tzinfo) - token.active_time > timedelta(seconds=self.timeout):
            token.delete()
            return False
        else:
            return True

class AccessToken(models.Model):
    objects = TokenManager()
    TokenTimeoutError: ClassVar[type[TokenTimeoutError]]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.CharField(max_length=10, default="windows")
    identification = models.CharField(max_length=64, default=partial(random_string_func, 64))
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    active_time = models.DateTimeField(default=timezone.now)