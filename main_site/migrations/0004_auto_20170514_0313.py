# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 20:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_auto_20170514_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalblog',
            name='noted',
            field=models.ManyToManyField(blank=True, related_name='noted', to='main_site.BlogPost', verbose_name='Прочитано'),
        ),
        migrations.AlterField(
            model_name='personalblog',
            name='feeds',
            field=models.ManyToManyField(blank=True, related_name='feeds', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
        migrations.AlterField(
            model_name='personalblog',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
        migrations.AlterField(
            model_name='personalblog',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='posts', to='main_site.BlogPost', verbose_name='Посты'),
        ),
    ]
