# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u5b66\u6b74')),
                ('graduated_on', models.DateField(help_text='\u9069\u5f53\u3067\u304a\uff4b', verbose_name='\u7d42\u4e86\u5e74\u6708\u65e5')),
                ('note', models.TextField(verbose_name='\u5099\u8003')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u30e6\u30fc\u30b6\u30fc\u5b66\u6b74\u60c5\u5831',
                'verbose_name_plural': '\u30e6\u30fc\u30b6\u30fc\u5b66\u6b74\u60c5\u5831',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u4fdd\u6709\u8cc7\u683c')),
                ('took_on', models.DateField(help_text='\u9069\u5f53\u3067\u304a\uff4b', verbose_name='\u53d6\u5f97\u5e74\u6708\u65e5')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u30e6\u30fc\u30b6\u30fc\u4fdd\u6709\u8cc7\u683c\u60c5\u5831',
                'verbose_name_plural': '\u30e6\u30fc\u30b6\u30fc\u4fdd\u6709\u8cc7\u683c\u60c5\u5831',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='generals',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u4f5c\u6210\u65e5\u6642'),
            preserve_default=True,
        ),
    ]
