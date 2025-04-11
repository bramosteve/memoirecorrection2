# Generated by Django 5.1.5 on 2025-04-05 03:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0012_groupmessage_encrypted_body_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='users_online',
            field=models.ManyToManyField(blank=True, related_name='online_in_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
