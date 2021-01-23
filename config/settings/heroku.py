import dj_database_url
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['overtrick.herokuapp.com']

ADMINS = (
    ('Kate McKenzie', 'kate.behind.the.web@gmail.com'),
)

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_FRAME_DENY = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 1000000
SECURE_SSL_REDIRECT = True

DATABASES = {
    'default': dj_database_url.config(conn_max_age=500, ssl_require=True)
}

STATICFILES_DIRS = [
    BASE_DIR / 'overtrick' / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
