# coding: utf8
from django.db import models
from django.contrib.auth.models import User

from apps.core.models import DateTime as AbstractDateTimeModel

class Generals(AbstractDateTimeModel):
    SEX_CHOICES = (
        (1, '男'),
        (2, '女'),
    )

    user = models.OneToOneField(User)
    birthday = models.DateField(u'生年月日')
    sex = models.SmallIntegerField(u'性別', choices=SEX_CHOICES)
    address = models.CharField(u'住所', max_length=200)
    station = models.CharField(u'最寄駅', max_length=200)
    note = models.TextField(u'ノート')

    def __unicode__(self):
        return u"<{}> id: {}".format(self.__class__.__name__, self.id)

    class Meta:
        verbose_name = verbose_name_plural = u"ユーザー基本情報"


class Educations(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(u'学歴', max_length=200)
    graduated_on = models.DateField(
        u'終了年月日',
        help_text=u'適当でおｋ'
    )
    note = models.TextField(u'備考')

    def __unicode__(self):
        return u"<{}> id: {}".format(self.__class__.__name__, self.id)

    class Meta:
        verbose_name = verbose_name_plural = u"ユーザー学歴情報"

class Licenses(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(u'保有資格', max_length=200)
    took_on = models.DateField(
        u'取得年月日',
        help_text=u'適当でおｋ'
    )

    def __unicode__(self):
        return u"<{}> id: {}".format(self.__class__.__name__, self.id)

    class Meta:
        verbose_name = verbose_name_plural = u"ユーザー保有資格情報"