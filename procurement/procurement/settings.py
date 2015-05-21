"""
Django settings for procurement project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'abdullahshah08@gmail.com'
EMAIL_HOST_PASSWORD = 'lovelymom'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oejt&bt#9$e40zu)vb#t@zcib8i1exyyhw_x+0b0gwh7aw5x6&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'crispy_forms',
    'orders',
    'customers',
    'contact',
    'bids',
    'consumers',
    'sellers',

)

ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'

#for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#django messagin framework with django_admin_bootstrapped
from django.contrib import messages

MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}

#for middleware 
SUBSCRIPTION_REQUIRED_URL = ['all_orders']
#SELLER_SPECIFIC_URL = ['bid']

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'procurement.middleware.CheckMembership',
    #'procurement.middleware.IsSeller',
)

ROOT_URLCONF = 'procurement.urls'

WSGI_APPLICATION = 'procurement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "static-dirs"),
    #'/Users/jmitch/Desktop/srvup/static/static_dirs/', #on mac
    #'\Users\jmitch\Desktop\srvup\static\static_dirs\', somethingl ike this on windows
    #'/var/www/static/',
)
STATIC_ROOT = os.path.join(BASE_DIR, "static", "static-only")

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")

