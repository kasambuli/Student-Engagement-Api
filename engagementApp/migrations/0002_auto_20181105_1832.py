# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engagementApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='highlighted',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
    ]