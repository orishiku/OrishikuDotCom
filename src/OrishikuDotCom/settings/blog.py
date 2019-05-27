from OrishikuDotCom.settings._base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
keyConfigs = SettingsFile(os.path.join(ROOT_DIR,'secrets','keys.txt'))

SECRET_KEY = keyConfigs.getKey('SECRET_KEY')

ALLOWED_HOSTS = ['blog.orishiku.com', ]

# Application definition

INSTALLED_APPS += []

ROOT_URLCONF = 'OrishikuDotCom.urls.blog'

WSGI_APPLICATION = 'OrishikuDotCom.wsgi.blog.application'

TEMPLATES[0]['DIRS'] += [
    os.path.join(BASE_DIR, 'OBlog', 'templates'),
]

STATICFILES_DIRS += []

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 2

keyConfigs = SettingsFile(os.path.join(ROOT_DIR,'secrets','mailgun.txt'))

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = keyConfigs.getKey('EMAIL')
EMAIL_HOST_PASSWORD = keyConfigs.getKey('PASSWORD')
EMAIL_USE_TLS = True
