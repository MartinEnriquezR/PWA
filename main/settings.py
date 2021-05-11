"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ak)1%32p4(wj78^3gw0s(dkp#yfn=)p$j55l71ch6^#q)xc@l('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#modificaciones en el user 
AUTH_USER_MODEL = 'sistema.Persona'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #aplicaciones creadas
    'catalogo',
    'sistema',
    'graficas',
    'notificaciones',
    #django rest framework
    'rest_framework',
    'rest_framework.authtoken',
    #CORS
    'corsheaders',
    #firebase cloud messaging
    'fcm_django',
]

#se elige la respuesta segun el orden en el que se enlistan
REST_FRAMEWORK={
    'DEFAULT_RENDERER_CLASSES':(
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
"""
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]
"""
CORS_ALLOW_ALL_ORIGINS=True

ROOT_URLCONF = 'main.urls'

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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'SISTEMA',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


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

#configuracion del servicio de correo 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_HOST_USER = 'ProyectoTerminal03@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


#configuracion del servicio de firebase cloud messaging
FCM_DJANGO_SETTINGS = {
         # default: _('FCM Django')
        "APP_VERBOSE_NAME": "Notificacion",
         # Your firebase API KEY
        "FCM_SERVER_KEY": "AAAAE749Ggs:APA91bHiyeGjV33SPArWZqxKAeU_bw1HmoGdoq2sWHRrjKix9JRDkZRgAXN5ayaeMtyQPyPMnXgCtClZNR_gLzUZDcwHG2I0gGjcnnEBVZQ6xlHpE5RDruRbuyZnj_MZzfK5QnqW5hWU",
         # true if you want to have only one active device per registered user at a time
         # default: False
        "ONE_DEVICE_PER_USER": False,
         # devices to which notifications cannot be sent,
         # are deleted upon receiving error response from FCM
         # default: False
        "DELETE_INACTIVE_DEVICES": False,
}

