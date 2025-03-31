# Generated by Django 5.1.5 on 2025-03-31 07:57

import django.db.models.deletion
import shortuuid.main
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0010_alter_chatgroup_users_online'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groupchats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='groupchat_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='users_online',
            field=models.ManyToManyField(blank=True, default=shortuuid.main.ShortUUID.uuid, related_name='online_in_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
