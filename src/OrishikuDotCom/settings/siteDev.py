from OrishikuDotCom.settings._baseDev import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
keyConfigs = SettingsFile(os.path.join(ROOT_DIR,'secrets','keys.txt'))

SECRET_KEY         = keyConfigs.getKey('SECRET_KEY')
GITHUB_WEBHOOK_KEY = keyConfigs.getKey('GITHUB_WEBHOOK_KEY')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS += [
    'OHook.apps.OhookConfig',
]
    
ROOT_URLCONF = 'OrishikuDotCom.urls.site'

WSGI_APPLICATION = 'OrishikuDotCom.wsgi.site.application'

TEMPLATES[0]['DIRS'] += []

STATICFILES_DIRS += []

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 1

