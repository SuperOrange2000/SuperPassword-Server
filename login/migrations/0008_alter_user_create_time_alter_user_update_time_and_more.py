# Generated by Django 4.2.6 on 2023-10-29 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_userlogintoken_active_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userlogintoken',
            name='active_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userlogintoken',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
