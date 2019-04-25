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

# Sites 
# https://docs.djangoproject.com/en/2.2/ref/contrib/sites/

SITE_ID = 1

# Fixtures
# https://code.djangoproject.com/wiki/Fixtures
FIXTURE_DIRS = [os.path.join(os.path.dirname(BASE_DIR), 'FIXTURES'),]