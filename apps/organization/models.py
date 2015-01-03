# coding: utf8
from django.db import models

from apps.core.models import DateTime as AbstractDateTimeModel


class Organization(AbstractDateTimeModel):
    name = models.CharField(u'組織名称', max_length=200)
    department = models.CharField(
        u'部門／部署等', max_length=200, null=True, blank=True)

    def __unicode__(self):
        return u'{} <{}>'.format(self.name, self.department)

    class Meta:
        verbose_name = verbose_name_plural = u'組織情報'
