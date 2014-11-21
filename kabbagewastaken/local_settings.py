__author__ = 'tim'

from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$z!1q42%!^94-_!v9=$dc8r0(95d0w7xf*o-@!f63a^ciqrl$n'

import os

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

