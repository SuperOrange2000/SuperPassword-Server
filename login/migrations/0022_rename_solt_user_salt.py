# Generated by Django 4.2.6 on 2024-02-07 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_rename_userlogintoken_accesstoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='solt',
            new_name='salt',
        ),
    ]