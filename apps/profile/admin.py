# coding: utf8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from apps.profile.models import General, Education, License


class GeneralInline(admin.StackedInline):
    model = General
    can_delete = False


class EducationInline(admin.TabularInline):
    model = Education


class LicenseInline(admin.TabularInline):
    model = License


class UserAdmin(UserAdmin):
    inlines = (GeneralInline, EducationInline, LicenseInline)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
