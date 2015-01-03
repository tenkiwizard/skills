# coding: utf8
"""
heroku用設定ファイル
"""
from apps.settings.base import *  # NOQA

INSTALLED_APPS += ('gunicorn', )

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config(default='postgres://localhost')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
