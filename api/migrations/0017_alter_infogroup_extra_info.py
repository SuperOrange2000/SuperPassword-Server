# Generated by Django 4.2.6 on 2024-09-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_infogroup_extra_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infogroup',
            name='extra_info',
            field=models.BinaryField(max_length=2048, null=True),
        ),
    ]