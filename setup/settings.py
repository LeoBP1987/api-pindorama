from pathlib import Path, os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'django_filters',
    'pindorama.apps.PindoramaConfig',
    'rest_framework',
    'storages',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if os.getenv('DJANGO_DEV'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': str(os.getenv('nome_bd')),
            'USER': str(os.getenv('usuario_bd')),
            'PASSWORD': str(os.getenv('senha_bd')),
            'HOST': str(os.getenv('host_bd')),
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
    'default': dj_database_url.config(
            default=os.environ['DATABASE_URL'],
            conn_max_age=600,
            ssl_require=True,
        )
    }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

#Configurando Arquivos Estáticos na AWS

if os.getenv('DJANGO_ENV') and os.getenv('DJANGO_ENV') == 'test':

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

else :

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "access_key": str(os.getenv("R2_ACCESS_KEY_ID")),
                "secret_key": str(os.getenv("R2_SECRET_ACCESS_KEY")),
                "bucket_name": str(os.getenv("R2_STORAGE_BUCKET_NAME")),
                "endpoint_url": "https://626ebd951efc663e718a48a8fcc0dce5.r2.cloudflarestorage.com/",
                "custom_domain": "pub-fea55699756d486f8aa6fd94cd7ef0fa.r2.dev",
                "location": "static",  
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "access_key": str(os.getenv("R2_ACCESS_KEY_ID")),
                "secret_key": str(os.getenv("R2_SECRET_ACCESS_KEY")),
                "bucket_name": str(os.getenv("R2_STORAGE_BUCKET_NAME")),
                "endpoint_url": "https://626ebd951efc663e718a48a8fcc0dce5.r2.cloudflarestorage.com/",
                "custom_domain": "pub-fea55699756d486f8aa6fd94cd7ef0fa.r2.dev",
                "location": "static", 
            },
        },
    }

    AWS_DEFAULT_ACL = 'public-read'

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    AWS_LOCATION = 'static'

    AWS_QUERYSTRING_AUTH = False

    AWS_HEADER = {
        'Access-Control-Allow-Origin': '*',
    }

    STATIC_URL = 'https://pub-fea55699756d486f8aa6fd94cd7ef0fa.r2.dev/static/'

    MEDIA_URL = 'https://pub-fea55699756d486f8aa6fd94cd7ef0fa.r2.dev/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:4173",
    "http://127.0.0.1:4173",
    "https://pindorama-front.vercel.app"
]