# Generated by Django 4.2.6 on 2024-09-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_alter_user_nickname_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.BinaryField(max_length=32),
        ),
    ]