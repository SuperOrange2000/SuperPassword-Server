# Generated by Django 4.2.6 on 2023-10-31 08:30

from django.db import migrations, models
import utils.random


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_user_create_time_alter_user_update_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='solt',
            field=models.CharField(default=utils.random.random_string_func, max_length=64),
        ),
    ]
