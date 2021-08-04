from .base import *

ALLOWED_HOSTS = [ '34.145.50.2' ] # customize with your domain name

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
