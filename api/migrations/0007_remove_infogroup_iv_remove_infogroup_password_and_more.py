# Generated by Django 4.2.6 on 2024-01-30 12:40

from django.db import migrations, models
import functools
import posix


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_infogroup_iv'),
    ]

    operations = [
        migrations.AddField(
            model_name='infogroup',
            name='data',
            field=models.BinaryField(default=b'', max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='infogroup',
            name='salt',
            field=models.BinaryField(default=functools.partial(posix.urandom, *(32,), **{}), max_length=32),
        ),
    ]
