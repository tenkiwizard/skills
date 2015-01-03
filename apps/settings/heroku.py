# coding: utf8
"""
heroku用設定ファイル
"""
from apps.settings.base import *  # NOQA

INSTALLED_APPS += ('gunicorn', )

# Parse database configuration from $DATABASE_URL
import dj_database_url
#DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
# ALLOWED_HOSTS = ['*']

# Static asset configuration
#import os
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
