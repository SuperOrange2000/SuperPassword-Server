# Generated by Django 4.2.6 on 2024-01-30 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_alter_user_check_code'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserLoginToken',
            new_name='AccessToken',
        ),
    ]