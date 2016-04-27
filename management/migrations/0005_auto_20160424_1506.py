# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 15:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0004_auto_20160328_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token_string', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userspaces',
            name='parent_space',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management.UserSpaces'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userspaces',
            name='space_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userspaces',
            name='space_type',
            field=models.IntegerField(choices=[(0, 'master'), (1, 'namespace'), (2, 'tenant')], max_length=256),
        ),
    ]
