from django.db import models
from functools import partial
import os

# Create your models here.
class InfoGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.BinaryField(max_length=64)
    password = models.BinaryField(max_length=64)
    site = models.BinaryField(max_length=64)
    tags = models.BinaryField(max_length=1024)
    extra_info = models.BinaryField(max_length=2048)
    salt = models.BinaryField(max_length=32, default=partial(os.urandom, 32))
    update_time = models.DateField(auto_now=True)
    create_time = models.DateField(auto_now_add=True)

class UserEntityRelation(models.Model):
    info_id = models.BigIntegerField(primary_key=False)
    info_group = models.ForeignKey(to=InfoGroup, on_delete=models.CASCADE)
    owner = models.ForeignKey(to="login.User", on_delete=models.CASCADE)