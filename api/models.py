from django.db import models
from functools import partial
import os

# Create your models here.
class InfoGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.BinaryField(max_length=2048)
    salt = models.BinaryField(max_length=32, default=partial(os.urandom, 32))
    update_time = models.DateField(auto_now=True)
    create_time = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(to="login.User", on_delete=models.CASCADE)
