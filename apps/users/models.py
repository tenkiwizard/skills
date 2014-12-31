# coding: utf8
from django.db import models
from django.contrib.auth.models import User as AuthUser

from apps.core.models import DateTime as AbstractDateTimeModel

class User(AbstractDateTimeModel):
    auth_user = models.OneToOneField(AuthUser)
    note = models.TextField(u'ノート')

    def __unicode__(self):
        return u"<{}> id: {}".format(self.__class__.__name__, self.id)

    class Meta:
        db_table = "users"
        verbose_name = verbose_name_plural = u"ユーザー"
