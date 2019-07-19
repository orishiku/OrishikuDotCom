from OrishikuDotCom.settings._base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
keyConfigs = SettingsFile(os.path.join(ROOT_DIR,'secrets','keys.txt'))

SECRET_KEY = keyConfigs.getKey('SECRET_KEY')

ALLOWED_HOSTS = ['demo.orishiku.com',]

# Application definition

INSTALLED_APPS += []

ROOT_URLCONF = 'OrishikuDotCom.urls.demo'

WSGI_APPLICATION = 'OrishikuDotCom.wsgi.demo.application'

TEMPLATES[0]['DIRS'] += []

STATICFILES_DIRS += []

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 3


