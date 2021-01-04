"""
Django settings for friendcodes project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    # Django: django-allauth, apps required.
    # https://django-allauth.readthedocs.io/en/latest/installation.html#django
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # easy-thumbnails: Application Added.
    # https://easy-thumbnails.readthedocs.io/en/latest/install/#configuring-your-project
    "easy_thumbnails",
    # django-import-export: Application Added.
    # https://django-import-export.readthedocs.io/en/latest/installation.html#installation-and-configuration
    "import_export",
    # django-bootstrap4: Application Added.
    # https://django-bootstrap4.readthedocs.io/en/latest/installation.html
    "bootstrap4",
    # django-storages: Application Added.
    # https://django-storages.readthedocs.io/en/latest/index.html#installation
    "storages",
    "core",
]
SITE_ID = 1
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "ordis.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                "django.template.context_processors.request",
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]
WSGI_APPLICATION = "ordis.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/")]
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Local-memory caching
# https://docs.djangoproject.com/en/2.2/topics/cache/#local-memory-caching
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "ordis-cache",
    }
}

# django-bootstrap4
# https://django-bootstrap4.readthedocs.io/en/latest/settings.html#settings
BOOTSTRAP4 = {
    # The complete URL to the Bootstrap CSS file
    # Note that a URL can be either a string,
    # e.g. "https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css",
    # or a dict like the default value below.
    "css_url": {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css",
        "integrity": "sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2",
        "crossorigin": "anonymous",
    },
    # The complete URL to the Bootstrap JavaScript file
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js",
        "integrity": "sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s",
        "crossorigin": "anonymous",
    },
    # The URL to the jQuery JavaScript file (full)
    "jquery_url": {
        "url": "https://code.jquery.com/jquery-3.5.1.min.js",
        "integrity": "sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=",
        "crossorigin": "anonymous",
    },
    # The URL to the jQuery JavaScript file (slim)
    "jquery_slim_url": {
        "url": "https://code.jquery.com/jquery-3.5.1.slim.min.js",
        "integrity": "sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs=",
        "crossorigin": "anonymous",
    },
    # The URL to the Popper.js JavaScript file (slim)
    "popper_url": {
        "url": "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js",
        "integrity": "sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN",
        "crossorigin": "anonymous",
    },
    # Set placeholder attributes to label if no placeholder is provided
    "set_placeholder": True,
}

# Django: Redirect on Login
# https://docs.djangoproject.com/en/3.1/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "feed"

# django-allauth: General Configuration
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = False  # Change for True in Production
ACCOUNT_EMAIL_VERIFICATION = "optional"  # Change for mandatory in Production
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"  # Change for https in Production
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_BLACKLIST = ["admin", "ordis", "cotizcesar", "Warframe"]
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_MIN_LENGTH = 6
REGISTRATION_OPEN = False  # Change for True in Production

THUMBNAIL_TRANSPARENCY_EXTENSION = "png"
THUMBNAIL_ALIASES = {
    "": {
        "userprofile_header": {"size": (960, 300), "crop": "smart", "upscale": True},
        "120x120": {"size": (120, 120), "crop": "smart", "upscale": True},
        "465x": {"size": (465, 0), "crop": "smart", "upscale": True},
        "36x36": {"size": (36, 36), "crop": "smart", "upscale": True},
        "475x125": {"size": (475, 125), "crop": "smart", "upscale": True},
        "48x48": {"size": (48, 48), "crop": "smart", "upscale": True},
        "283x": {"size": (283, 0), "crop": "smart", "upscale": True},
        "298x167": {"size": (298, 167), "crop": "smart", "upscale": True},
        "559x": {"size": (559, 0), "crop": "smart", "upscale": True},
        "1200x630": {"size": (1200, 630), "crop": "smart", "upscale": True},
        "avatar": {"size": (510, 510), "crop": "smart", "upscale": True},
        "post": {"size": (540, 0), "crop": "smart", "upscale": True},
        "order": {"size": (74, 74), "crop": "smart", "upscale": True},
        "item": {"size": (510, 287), "crop": "smart", "upscale": True},
        "warframe": {"size": (510, 906), "crop": "smart", "upscale": True},
        "warframe_detail": {"size": (510, 906), "crop": "smart", "upscale": True},
        "warframe_list": {"size": (510, 287), "crop": "0,0", "upscale": True},
        "warframe_market_list": {"size": (510, 287), "crop": "0,0", "upscale": True},
        "warframe_50x50": {"size": (50, 50), "crop": "0,0", "upscale": True},
        "44x44": {"size": (44, 44), "crop": "smart", "upscale": True},
        "50x50": {"size": (50, 50), "crop": "smart", "upscale": True},
        "66x66": {"size": (66, 66), "crop": "smart", "upscale": True},
        "warframe_66x66": {"size": (66, 66), "crop": "0,0", "upscale": True},
        "89x89": {"size": (89, 89), "crop": "smart", "upscale": True},
        "510x287": {"size": (510, 287), "crop": "smart", "upscale": True},
    },
}
THUMBNAIL_NAMER = "easy_thumbnails.namers.hashed"

"""
# django-storages
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
THUMBNAIL_DEFAULT_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_REGION_NAME = os.environ["AWS_S3_REGION_NAME"]
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
"""

# Activate Django-Heroku.
django_heroku.settings(locals())