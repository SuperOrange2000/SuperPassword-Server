from django.db import models
from functools import partial
import os

# Create your models here.
class InfoGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    sub_id = models.CharField(max_length=32)
    site = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    iv = models.BinaryField(max_length=16, default=partial(os.urandom, 16))
    tags = models.JSONField()
    update_time = models.DateField(auto_now=True)
    create_time = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(to="login.User", on_delete=models.CASCADE)
