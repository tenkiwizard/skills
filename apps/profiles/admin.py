# coding: utf8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from apps.profiles.models import Generals, Educations, Licenses


class GeneralsInline(admin.StackedInline):
    model = Generals
    can_delete = False


class EducationsInline(admin.TabularInline):
    model = Educations


class LicensesInline(admin.TabularInline):
    model = Licenses


class UserAdmin(UserAdmin):
    inlines = (GeneralsInline, EducationsInline, LicensesInline)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
