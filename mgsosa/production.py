from .base import *

ALLOWED_HOSTS = [ '34.66.85.93' ] # customize with your domain name

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mgsosa',
        'USER': 'mgsosa',
        'PASSWORD': 'Mava@12345',
        'HOST' : 'localhost,
        'PORT' : '3306'
    }
}

STATIC_ROOT = '/home/ubuntu/Mgsosa/static'
