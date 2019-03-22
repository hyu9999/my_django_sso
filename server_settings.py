import os

from sso.settings.base import *  # noqa
DEBUG = True
ALLOWED_HOSTS = ['49.4.7.114', '127.0.0.1']

STATIC_ROOT = '/home/www/sso_server/static'
MEDIA_ROOT = '/home/www/sso_server/media'

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'sso',
       'USER':'postgres',
       'PASSWORD': 'mint@2016',
       'HOST': '39.130.160.107'
    }
}

from django.core.cache import cache
cache.set('mine', '49.4.7.114')
m = cache.get('mine')
print("test cache================================",m)