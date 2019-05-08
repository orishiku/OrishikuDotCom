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
    'OBlog.apps.OblogConfig',
    ]

ROOT_URLCONF = 'OrishikuDotCom.urls.site'

TEMPLATES[0]['DIRS'] += []

STATICFILES_DIRS += []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 1

# OPages 
DEFAULT_TEMPLATE = 'Pages/default.html'