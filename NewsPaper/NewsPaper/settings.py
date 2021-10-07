"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import secrets
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oa$qc9ww&@9!hkgwc$tfh5+=3)i7)n$*m1_$kr(9=2@f#^hqds'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'django_filters',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

SITE_ID = 1

ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_FORMS = {'signup': 'news.forms.CommonSignupForm'}


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'Forz00'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'Forz00@yandex.by'
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           'allauth.account.auth_backends.AuthenticationBackend',]

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

LOGGING = {'version': 1,
           'disable_existing_loggers': False,
           'style': '{',
           'formatters': {
               'debug': {
                   'format': '%(asctime)s %(levelname)s %(message)s'
               },
               'warning': {
                   'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
               },
               'error': {
                   'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
               },
               'general_sec_log': {
                   'format': '%(asctime)s %(levelname)s %(module)s %(message)s '
               },
               'mail_log': {
                   'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
               }
           },
           'filters': {
               'require_debug_true': {
                   '()': 'django.utils.log.RequireDebugTrue'
               },
               'require_debug_false': {
                   '()': 'django.utils.log.RequireDebugFalse'
               },
           },
           'handlers': {
               'console_debug': {
                   'level': 'DEBUG',
                   'filters': ['require_debug_true'],
                   'class': 'logging.StreamHandler',
                   'formatter': 'debug'
               },
               'console_warning': {
                   'level': 'WARNING',
                   'filters': ['require_debug_true'],
                   'class': 'logging.StreamHandler',
                   'formatter': 'warning'
               },
               'console_error': {
                   'level': 'ERROR',
                   'filters': ['require_debug_true'],
                   'class': 'logging.StreamHandler',
                   'formatter': 'error'
               },
               'console_critical': {
                   'level': 'CRITICAL',
                   'filters': ['require_debug_true'],
                   'class': 'logging.StreamHandler',
                   'formatter': 'error'
               },
               'log_gen_info': {
                   'level': 'INFO',
                   'filters': ['require_debug_false'],
                   'class': 'logging.FileHandler',
                   'filename': 'general.log',
                   'formatter': 'general_sec_log'
               },
               'log_sec_info': {
                   'level': 'INFO',
                   'class': 'logging.FileHandler',
                   'filename': 'security.log',
                   'formatter': 'general_sec_log'
               },
               'log_err_error': {
                   'level': 'ERROR',
                   'class': 'logging.FileHandler',
                   'filename': 'errors.log',
                   'formatter': 'error'
               },
               'mail_error': {
                   'level': 'ERROR',
                   'filters': ['require_debug_false'],
                   'class': 'django.utils.log.AdminEmailHandler',
                   'formatter': 'mail_log'
               }


           },
           'loggers': {
               'django': {
                   'handlers': ['console_debug', 'console_warning', 'console_error', 'log_gen_info'],
                   'propagate': True
               },
               'django.request': {
                   'handlers': ['log_err_error', 'console_critical', 'mail_error'],
                   'propagate': True
               },
               'django.server': {
                   'handlers': ['log_err_error', 'console_critical', 'mail_error'],
                   'propagate': True
               },
               'django.template': {
                   'handlers': ['log_err_error', 'console_critical'],
                   'propagate': True
               },
               'django.db_backends': {
                   'handlers': ['log_err_error', 'console_critical'],
                   'propagate': True
               },
               'django.security': {
                   'handlers': ['log_sec_info'],
                   'propagate': True
               },

           }
           }









