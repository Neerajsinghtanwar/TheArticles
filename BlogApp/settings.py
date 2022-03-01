"""
Django settings for BlogApp project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zo9l28+lajrfw1vezmyu!-*$6i$$ssy*&ase)m#4&6m44odjax'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False   # For production
#
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['15.206.147.220']   # For production

# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    'rest_framework',
    'blog',
    'accounts',
    'notifications',
    'ckeditor',
    'ckeditor_uploader',
    'webpack_loader',
    'django_celery_beat',
    # 'debug_toolbar'

]

CKEDITOR_UPLOAD_PATH = 'uploads/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BlogApp.urls'

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

WSGI_APPLICATION = 'BlogApp.wsgi.application'
ASGI_APPLICATION = 'BlogApp.asgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'the_article_db',
        'USER': 'postgresuser',
        'PASSWORD': 'password123',
        'HOST': 'localhost'
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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_DIR = os.path.join(BASE_DIR, 'templates', 'static')

STATICFILES_DIRS = [STATIC_DIR]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}


MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'extraPlugins': 'codesnippet',
    },
}

CORS_ORIGIN_ALLOW_ALL = False

# CORS_ALLOW_CREDENTIALS = True
#
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "http://the-aarticles.herokuapp.com/signup",
    "https://the-aarticles.herokuapp.com/signup",
]

CORS_ORIGIN_REGEX_WHITELIST = [
    "http://localhost:3000",
    "http://the-aarticles.herokuapp.com/signup",
    "https://the-aarticles.herokuapp.com/signup",
]

# Define token expiry time in simple jwt:-
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=10),  # This object is to set the expiry time of verify token
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # This object is to set the expiry time of refresh token
    # 'ROTATE_REFRESH_TOKENS':True    # This object is regenerate a new refresh token when we refresh

}

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'theaarticles@gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'Asdfghjkl@12'
EMAIL_USE_TLS = True

import django
django.setup()

