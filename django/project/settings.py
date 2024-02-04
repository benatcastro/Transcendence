"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os, environ
from datetime import timedelta

# Init env variable handler
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-o&5&cg&s$mziwz^o2gb=p2^pb3_l8wh8+y+%0&@d_n45nx!jd5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    'watchman',
    'daphne',
    "django.contrib.staticfiles",
    "transcendence",
    'django_extensions',
    'users',
    'friends',
    'intra_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'rest_auth',
    'channels',
    'django_prometheus',
    'drf_yasg',
    'matchmaking',
    'game',
    
]

MIDDLEWARE = [
 'django_prometheus.middleware.PrometheusBeforeMiddleware',  #importante que este middleware este colocado el primero
 'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "project.middleware.MyMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    'django_prometheus.middleware.PrometheusAfterMiddleware',  #importante que este middleware este colocado el ultimo
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
        'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': env('GOOGLE_UID'),
            'secret': env('GOOGLE_SECRET'),
            'key': ''
        }
    },
    '42intra': {
        'SCOPE': [
            'public'
        ],
        'APP': {
            'client_id': env('INTRA_UID'),
            'secret': env('INTRA_SECRET'),
            'key': ''
        }
    }
}

SITE_ID = 1


SLIDING_TOKEN_LIFETIME = timedelta(hours=4),

ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'transcendence-jwt',
    'JWT_AUTH_REFRESH_COOKIE': 'transcendence-refresh-jwt',
}

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

FRONTEND_LOGIN_CALLBACK = 'frontend:5173/mockups/callback'

REST_USE_JWT = True

MIDDLEWARE_CLASSES = (
    'livesync.core.middleware.DjangoLiveSyncMiddleware',
)

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'transcendence', 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

RUNSERVERPLUS_POLLER_RELOADER_INTERVAL = 1
RUNSERVERPLUS_POLLER_RELOADER_TYPE = 'auto'
WSGI_APPLICATION = "project.wsgi.application"
ASGI_APPLICATION = "project.asgi.application"

WHITENOISE_AUTOREFRESH = True  # Habilita la actualización en tiempo real para archivos estáticos

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': env('ENGINE'),

        'NAME': env('DB_NAME'),

        'USER': env('POSTGRES_USER'),

        'PASSWORD': env('POSTGRES_PASSWORD'),

        'HOST': env('DB_HOST'),

        'PORT': env('DB_PORT'),

    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Users
AUTH_USER_MODEL = 'users.TranscendenceUser'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# CORS

SESSION_COOKIE_SAMESITE = 'None'
CORS_ALLOW_HEADERS = (
     "accept",
     "authorization",
     "content-type",
     "user-agent",
     "x-csrftoken",
     "x-requested-with",
)


CORS_ALLOW_CREDENTIALS = True

# CON ESTO ALGUNA VARIBLES DE GET NO PASAN DE FRONTEND A BACKED
CORS_ALLOWED_HOSTS = [
    'https://localhost:443',
    'https://frontend:5173',
    'http://frontend:5173',
    'http://localhost',
]

CORS_ALLOWED_ORIGINS = [
    'https://localhost:443',
    'https://localhost',
    'https://frontend:5173',
    'http://frontend:5173',
    'http://localhost',

]

CSRF_TRUSTED_ORIGINS = [
    'https://localhost'
]

# CORS_ALLOWED_HOSTS = ["*"]
# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_ALL_ORIGINS = True
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}

SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
