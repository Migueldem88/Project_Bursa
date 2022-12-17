from .base import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TYPE YOUR DB NAME',
        'USER': 'TYPE YOUR USER NAME',
        'PASSWORD': 'TYPE YOUR PASSWORD',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'static/'

#https://www.youtube.com/watch?v=UKE5yQAmg0k