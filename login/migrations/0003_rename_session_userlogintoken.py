# Generated by Django 4.2.6 on 2023-10-29 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_session_create_time_alter_user_profile_pic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Session',
            new_name='UserLoginToken',
        ),
    ]
