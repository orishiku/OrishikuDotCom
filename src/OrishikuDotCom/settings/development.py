from OrishikuDotCom.settings._base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key-dev'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS += [
    'django.contrib.flatpages',
    'OBlog.apps.OblogConfig',
    'OPages.apps.OpagesConfig',
    ]

ROOT_URLCONF = 'OrishikuDotCom.urls.site'

TEMPLATES[0]['DIRS'] += []

STATICFILES_DIRS += []

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 1

# OPages 
DEFAULT_TEMPLATE = 'Pages/default.html'