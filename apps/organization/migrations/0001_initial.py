# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u6642')),
                ('name', models.CharField(max_length=200, verbose_name='\u7d44\u7e54\u540d\u79f0')),
                ('department', models.CharField(max_length=200, null=True, verbose_name='\u90e8\u9580\uff0f\u90e8\u7f72\u7b49', blank=True)),
            ],
            options={
                'verbose_name': '\u7d44\u7e54\u60c5\u5831',
                'verbose_name_plural': '\u7d44\u7e54\u60c5\u5831',
            },
            bases=(models.Model,),
        ),
    ]
