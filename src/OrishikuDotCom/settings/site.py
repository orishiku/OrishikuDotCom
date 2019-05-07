from OrishikuDotCom.settings._base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key-site'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['orishiku.com', 'www.orishiku.com']

# Application definition

INSTALLED_APPS += [
    'django.contrib.flatpages',
    'OPages.apps.OpagesConfig',
]

ROOT_URLCONF = 'OrishikuDotCom.urls.site'

WSGI_APPLICATION = 'OrishikuDotCom.wsgi.site.application'

TEMPLATES[0]['DIRS'] += []

STATICFILES_DIRS += []

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 1

# OPages 
DEFAULT_TEMPLATE = 'Pages/default.html'
if not DEBUG:
    SECURE_PROXY_SSL_HEADER        = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT            = True
    SESSION_COOKIE_SECURE          = True
    CSRF_COOKIE_SECURE             = True
    SECURE_HSTS_SECONDS            = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF    = True
    SECURE_BROWSER_XSS_FILTER      = True
    X_FRAME_OPTIONS                = 'DENY'
    SECURE_HSTS_PRELOAD            = True
