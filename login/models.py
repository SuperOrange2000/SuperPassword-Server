from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nick_name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    solt = models.CharField(max_length=64)
    profile_pic = models.ImageField()
    update_time = models.DateField(auto_now=True)
    create_time = models.DateField(auto_now_add=True)

class Session(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.CharField(max_length=10)
    identification = models.CharField(max_length=64)
    create_time = models.DateField(auto_now_add=True)
    active_time = models.DateField()