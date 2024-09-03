from django.db import models
from functools import partial
from login.models import User
import os

# Create your models here.
class InfoGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    guid = models.CharField(max_length=36)

    site = models.BinaryField(max_length=64)
    username = models.BinaryField(max_length=64)
    password = models.BinaryField(max_length=64)
    extra_info = models.BinaryField(max_length=2048, null=True)
    update_time = models.DateField(auto_now=True)
    create_time = models.DateField(auto_now_add=True)

    owner = models.ForeignKey("login.User", on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=["guid"])
        ]

class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    guid = models.CharField(max_length=36)

    content = models.BinaryField(max_length=64)

    info_group = models.ForeignKey(to=InfoGroup, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=["guid"])
        ]