"""
Django settings for hita project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u)g)xrvthc6#b07ndf%^b$e=#r^)%7ca@16-q8&j*=ixgzx$n7'

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
    'management',
    'api',
    'namespaces',
    'tenant',
    'dashboards',
    'payment',
    'rest_framework_swagger',
    'rest_framework',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hita.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'hita.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = os.path.join(BASE_DIR, 'themes/')

STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'themes/'), )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'themes/'),
        ],
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

ENV_NUMBER = 2

ENVIRONMENTS = ["PRODUCTION","TEST","DEVELOPMENT"]
ENVIRONMENT = ENVIRONMENTS[ENV_NUMBER]

ENVIRONMENT_URLS = ["https://192.241.219.84/","https://192.241.219.84/","http://127.0.0.1:8000/"]
ENVIRONMENT_URL = ENVIRONMENT_URLS[ENV_NUMBER]

AUTH_KEY = "bXNheWdp:65f612d5e6bfba42b9961bf2767e7b5d"

# E-Mail Configurations

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'xxxxxx@xxxx.com'
EMAIL_HOST_PASSWORD = 'xxxxxx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# HCP Configurations

MAIN_IP = "192.168.1.51"

MASTER_USER = "security"
MASTER_PASS = "xxxxxx"

# End Of HCP Configurations

# Asecco Credit Card Integration

EST_MERCHANT_ID = "400000200"
EST_3D_KEY = "TRPS0200"
EST_RETURN_URL = ENVIRONMENT_URL+"payment/success/"
EST_FAIL_URL = ENVIRONMENT_URL+"payment/fail/"
EST_3D_URL = 'https://entegrasyon.asseco-see.com.tr/fim/est3Dgate'

# End Of Integration

# Paypal Integration

CLIENT_ID = "AYXqb1j2oR2iw2PXh6Wji74ZqYH9xlGdr9-3kASp94ydkB61WG6qHXxcseSMjhYNHh7NHt8vvJ2FoDfJ"
CLIENT_SECRET = "EGyU3h7wd7r1RCxwsutW_v8qUK4ZKyMbX1NPZVnZGJg5bq1Gf-DKM-LQNF9frgfGjSnSUBOSN6XyOCVQ"

# End Of Integration
