from OrishikuDotCom.settings._base import *
from OrishikuDotCom.settings.utils import ConfigFile

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
keyConfigs = ConfigFile(os.path.join(ROOT_DIR,'secrets','keys.txt'))

SECRET_KEY = keyConfigs.getKey('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['blog.orishiku.com', 'localhost']

# Application definition

INSTALLED_APPS += [
    'OBlog.apps.OblogConfig',
    ]

ROOT_URLCONF = 'OrishikuDotCom.urls.blog'

WSGI_APPLICATION = 'OrishikuDotCom.wsgi.blog.application'

TEMPLATES[0]['DIRS'] += [
    os.path.join(BASE_DIR, 'OBlog', 'templates'),
]

STATICFILES_DIRS += []

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 2