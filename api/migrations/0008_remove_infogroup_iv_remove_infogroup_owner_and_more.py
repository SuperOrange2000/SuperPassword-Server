# Generated by Django 4.2.6 on 2024-02-03 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0021_rename_userlogintoken_accesstoken'),
        ('api', '0007_remove_infogroup_iv_remove_infogroup_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infogroup',
            name='owner',
        ),
        migrations.CreateModel(
            name='UserEntityRelation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('info_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.infogroup')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user')),
            ],
        ),
    ]