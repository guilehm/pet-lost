from petLost.settings import *

DEBUG = True
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS += [
    '127.0.0.1',
    '.localhost',
]

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
