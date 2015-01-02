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
            name='Generals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
                ('birthday', models.DateField(verbose_name='\u751f\u5e74\u6708\u65e5')),
                ('sex', models.SmallIntegerField(verbose_name='\u6027\u5225', choices=[(1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3')])),
                ('address', models.CharField(max_length=200, verbose_name='\u4f4f\u6240')),
                ('station', models.CharField(max_length=200, verbose_name='\u6700\u5bc4\u99c5')),
                ('note', models.TextField(verbose_name='\u30ce\u30fc\u30c8')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u30e6\u30fc\u30b6\u30fc\u57fa\u672c\u60c5\u5831',
                'verbose_name_plural': '\u30e6\u30fc\u30b6\u30fc\u57fa\u672c\u60c5\u5831',
            },
            bases=(models.Model,),
        ),
    ]
