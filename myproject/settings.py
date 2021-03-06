"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.3.
"""
import os
from django.urls import path, include
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# security key
import dotenv

# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(BASE_DIR, ".env")

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Update secret key
SECRET_KEY = str(os.getenv('SECRET_KEY'))

cloudinary.config(
  cloud_name = str(os.getenv('CLOUD_NAME')),
  api_key = str(os.getenv('API_KEY')),
  api_secret = str(os.getenv('API_SECRET'))
)




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_seed',
    'cloudinary_storage',
    'cloudinary',
    'compressor',
    'myproject',
    'mycv'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


import dj_database_url


DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)

MEDIA_URL = '/public/'  # or any prefix you choose (I generally like it to be 'public')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

ALLOWED_HOSTS = [
    '*',
]

###
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "assets"),
    os.path.join(BASE_DIR, "node_modules"),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

COMPRESS_OFFLINE = False

COMPRESS_OUTPUT_DIR = ''

try:
    from local_settings import *
except ImportError:
    pass

NODE_ENV = 'development' if DEBUG else 'production'

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'node_modules/.bin/node-sass {infile} {outfile}'),
    ('text/jsx', 'NODE_ENV={} node_modules/.bin/browserifyinc '
                 '--debug '
                 '-t babelify {{infile}} -o {{outfile}}'.format(NODE_ENV)),
)

if not DEBUG:
    COMPRESS_OFFLINE = True
    COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'node_modules/.bin/node-sass {infile} {outfile}'),
    ('text/jsx', 'NODE_ENV=production node_modules/.bin/browserify '
                 '-t babelify {infile} -o {outfile}'),
)
