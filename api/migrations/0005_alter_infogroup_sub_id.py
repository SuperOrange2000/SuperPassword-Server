# Generated by Django 4.2.6 on 2023-10-31 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_website_infogroup_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infogroup',
            name='sub_id',
            field=models.CharField(max_length=32),
        ),
    ]