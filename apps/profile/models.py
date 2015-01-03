# coding: utf8
from django.db import models
from django.contrib.auth.models import User

from apps.organization.models import Organization
from apps.core.models import DateTime as AbstractDateTimeModel

class General(AbstractDateTimeModel):
    SEX_CHOICES = (
        (1, '男'),
        (2, '女'),
    )

    user = models.OneToOneField(User)
    organization = models.ForeignKey(
        Organization, null=True, blank=True, verbose_name=u'所属')
    birthday = models.DateField(u'生年月日')
    sex = models.SmallIntegerField(u'性別', choices=SEX_CHOICES)
    address = models.CharField(u'住所', max_length=200)
    station = models.CharField(u'最寄駅', max_length=200)
    note = models.TextField(u'ノート')

    def __unicode__(self):
        return u'{} {} ({} : {})'.format(
            self.user.last_name, self.user.first_name,
            self.organization.name, self.organization.department
        )

    class Meta:
        verbose_name = verbose_name_plural = u'ユーザー基本情報'


class Education(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(u'学歴', max_length=200)
    graduated_on = models.DateField(
        u'終了年月日',
        help_text=u'適当でおｋ'
    )
    note = models.TextField(u'備考')

    def __unicode__(self):
        return u'{} (〜{})'.format(self.name, self.graduated_on)

    class Meta:
        verbose_name = verbose_name_plural = u'ユーザー学歴情報'

class License(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(u'保有資格', max_length=200)
    took_on = models.DateField(
        u'取得年月日',
        help_text=u'適当でおｋ'
    )

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.took_on)

    class Meta:
        verbose_name = verbose_name_plural = u'ユーザー保有資格情報'
