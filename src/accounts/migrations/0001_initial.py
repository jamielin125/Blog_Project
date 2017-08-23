# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-23 01:20
from __future__ import unicode_literals

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='default-user-image.png', height_field='height_field', null=True, upload_to=accounts.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=50)),
                ('width_field', models.IntegerField(default=50)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
