# Heroku Production Settings
import os

DEBUG = True

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    'default':  dj_database_url.config()
}

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

from .base_settings import *
