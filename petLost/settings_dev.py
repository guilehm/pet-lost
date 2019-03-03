from petLost.settings import *

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
