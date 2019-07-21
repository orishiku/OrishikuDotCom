from OrishikuDotCom.settings._baseDev import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
keyConfigs = SettingsFile(os.path.join(ROOT_DIR,'secrets','keys.txt'))

SECRET_KEY = keyConfigs.getKey('SECRET_KEY')

ALLOWED_HOSTS = ['dev.orishiku','localhost']

# Application definition

INSTALLED_APPS += ['trackingDemo',]
    
ROOT_URLCONF = 'OrishikuDotCom.urls.demo'

WSGI_APPLICATION = 'OrishikuDotCom.wsgi.demo.application'

TEMPLATES[0]['DIRS'] += []

STATICFILES_DIRS += []

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 3

FIREBASE_KEY = os.path.join(ROOT_DIR, "secrets", 
                            "trackingpipe-firebase-adminsdk-wsqc0-e8758c4a92.json")
