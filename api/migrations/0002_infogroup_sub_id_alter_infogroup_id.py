# Generated by Django 4.2.6 on 2023-10-30 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infogroup',
            name='sub_id',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infogroup',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
