# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
                ('note', models.TextField(verbose_name='\u30ce\u30fc\u30c8')),
                ('auth_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users',
                'verbose_name': '\u30e6\u30fc\u30b6\u30fc',
                'verbose_name_plural': '\u30e6\u30fc\u30b6\u30fc',
            },
            bases=(models.Model,),
        ),
    ]
