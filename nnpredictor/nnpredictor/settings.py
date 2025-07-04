"""
Django settings for nnpredictor project.

Generated by 'django-admin startproject' using Django 5.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i#ln!$k2!k-asipsf14jd#a$2l2063gjt%6yl9(3o2&ed#=9i%'

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
    'rest_framework',
    'uvicorn',
    'drf_spectacular',
    'predictionserver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nnpredictor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION = 'nnpredictor.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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

# Настройки DRF
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# Опциональные настройки drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'PredictionServer API',
    'DESCRIPTION': 'Прогнозирование многомерных временных рядов по датчикам буровой установки. Включает в себя единственный POST-запрос.',
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': False,
}


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Constants
MODELS_DIR = os.path.join(BASE_DIR, 'predictionserver', 'nn_models')
EXIT_LENGTH = 120
FIELDS = ['wellDepth', 'bitDepth', 'wOB', 'sPP', 'flowRateIn', 'surfaceTorque', 'surfaceRPM', 'blockPosition', 'trippingSpeed', 'rOP']
FEATURES_TOTAL = len(FIELDS)
REQ_LENGTH_INPUT = 600
MEANS = {"wellDepth" : 823.2375705988211, "bitDepth" : 509.99035448548574, "wOB" : 0.35424483686138347, "sPP" : 22.46055188219852, "flowRateIn" : 8.436832413606632, "surfaceTorque" : 2.004083127911857, "surfaceRPM" : 9.864737685724593, "blockPosition" : 12.258214255042056, "trippingSpeed" : 0.0323337854956623, "rOP" : 38.85209902392712}
STDS = {"wellDepth" : 357.65324119764614, "bitDepth" : 389.88514874229276, "wOB" : 1.263494967993503, "sPP" : 37.72799034848868, "flowRateIn" : 14.903409964648077, "surfaceTorque" : 2.809720676366944, "surfaceRPM" : 20.92180449797566, "blockPosition" : 8.900226107657316, "trippingSpeed" : 0.10568595969692353, "rOP" : 32.45560604866986}