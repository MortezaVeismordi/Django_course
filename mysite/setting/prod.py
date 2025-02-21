from mysite.settings import *

SECRET_KEY = 'django-insecure-q_(wb_y#v1x3t9u&reoa)7k+h&1!1($+tj+o4bdgyjcn^3n@hh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

SITE_ID=2

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

# X_FRAME_OPTIONS = 'SAMEORIGIN'

# CSRF_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True