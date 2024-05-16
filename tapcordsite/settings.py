"""
Django settings for tapcordsite project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv
import dj_database_url


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!



DEBUG = os.getenv("DEBUG" "True") == "True"



ALLOWED_HOSTS = ["https://tapcord.onrender.com", 'tapcord.onrender.com', 'localhost', '127.0.0.1', '::1']

# if DEBUG == "True" :
#     ALLOWED_HOSTS = []

#     print(f'this is the debug {DEBUG}')
    
# else:
#     ALLOWED_HOSTS = ['tapcord.onrender.com', 'localhost', '127.0.0.1']
#     print(f'debug is {DEBUG} here')
# ALLOWED_HOSTS = ['https://presictravels.herokuapp.com/', 'http://presictravels.herokuapp.com/', '127.0.0.1']

# Application definition

print(f'this is the value of Debug in production: {DEBUG} ')

INSTALLED_APPS = [
    'tapcord',
    'blog',

    'ckeditor',
    'ckeditor_uploader',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # added the whitenoise to be able to serve static files on deployment
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tapcordsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'tapcordsite/templates/tapcordsite'),
            os.path.join(BASE_DIR, 'blog/templates/blog')

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

WSGI_APPLICATION = 'tapcordsite.wsgi.application'


# Database

# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

DATABASES = {
    'default': {
    'ENGINE': 'website_postgress_tapcord',
    'NAME': 'website-posgresql-presictravels',
    'USER': USER,
    'PASSWORD': PASSWORD, # Replace with the actual password
    'HOST': 'dpg-cp2almn79t8c73fq5nd0-a',

    'PORT': '5432',
    }

}

DATABASE_URL = os.getenv('DATABASE_URL ')
# DATABASES = {
#     'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
#     }

# this will enable database update from development environmet
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)



# DATABASES = {
#     'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
#     }



# for email smtp
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = 'frankmadu2live@gmail.com'
EMAIL_HOST_PASSWORD = 'bhtm tcvp cbis hbja'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



#ckeditor 
CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'
# compreser for deployment


STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

# this helps to logg in bugs even when Debug is set to False
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # 'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            #'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'tapcordsite/static/'),
    
]

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
