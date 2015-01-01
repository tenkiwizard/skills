# coding: utf8
from django.contrib import admin

from apps.profiles.models import Generals, Educations, Licenses

admin.site.register(Generals)
admin.site.register(Educations)
admin.site.register(Licenses)
