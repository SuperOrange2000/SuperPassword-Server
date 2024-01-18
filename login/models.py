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
    nickname = models.CharField(max_length=32, default=partial(random_string_func, 8))
    username = models.CharField(max_length=32, default=partial(random_string_func, 8))
    check_code = models.BinaryField(max_length=128)
    iv = models.BinaryField(max_length=16, default=partial(os.urandom, 16))
    solt = models.CharField(max_length=64, default=random_string_func)
    profile_pic = models.ImageField(upload_to="profile_pic", storage=HashStorage(), default="profile_pic/default.png")
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True, editable=False)

class TokenManager(models.Manager):
    timeout = 300
    def get(self, *args, **kwargs):
        token = super().get(*args, **kwargs)
        if self.check_timeout(token):
            token.active_time = datetime.now(token.active_time.tzinfo)
            token.save()
            return True, token
        else:
            return False, None

    def check_timeout(self, token) -> list[Any]:
        if datetime.now(token.active_time.tzinfo) - token.active_time > timedelta(seconds=self.timeout):
            return False
        else:
            return True

class UserLoginToken(models.Model):
    objects = TokenManager()
    TokenTimeoutError: ClassVar[type[TokenTimeoutError]]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.CharField(max_length=10, default="windows")
    identification = models.CharField(max_length=64, default=partial(random_string_func, 64))
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    active_time = models.DateTimeField(default=timezone.now)