# Heroku Production Settings

DEBUG = True

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    'default':  dj_database_url.config()
}

from .base_settings import *
