# Generated by Django 5.1.5 on 2025-03-23 09:39

import shortuuid.main
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0005_alter_chatgroup_users_online'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='users_online',
            field=models.ManyToManyField(blank=True, default=shortuuid.main.ShortUUID.uuid, related_name='online_in_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
