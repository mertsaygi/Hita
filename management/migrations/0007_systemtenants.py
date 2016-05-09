# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-28 21:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0006_auto_20160424_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemTenants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('space_url', models.URLField()),
                ('space_name', models.CharField(max_length=255)),
                ('space_type', models.IntegerField(choices=[(1, 'namespace'), (2, 'tenant')])),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'System Tenants',
            },
        ),
    ]