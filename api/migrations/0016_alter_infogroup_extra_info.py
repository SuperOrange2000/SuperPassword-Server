# Generated by Django 4.2.6 on 2024-09-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_infogroup_password_nonce_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infogroup',
            name='extra_info',
            field=models.BinaryField(blank=True, max_length=2048),
        ),
    ]