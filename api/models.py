from django.db import models

# Create your models here.
class InfoGroup(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    tags = models.JSONField()
    update_time = models.DateField(auto_now=True)
    create_time = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(to="login.User", on_delete=models.CASCADE)
