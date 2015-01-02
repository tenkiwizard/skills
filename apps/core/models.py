# coding: utf8
from django.db import models
from django.utils import timezone

class DateTime(models.Model):
    created = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated = models.DateTimeField(u'更新日時', auto_now=True)

    class Meta:
        abstract = True
