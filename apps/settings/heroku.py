# coding: utf8
"""
heroku用設定ファイル
"""
from apps.settings.base import *  # NOQA

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
