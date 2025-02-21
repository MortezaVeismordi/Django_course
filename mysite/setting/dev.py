from mysite.settings import *


DEBUG = True

# دامنه‌های مجاز در محیط توسعه
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# تنظیمات امنیتی برای محیط توسعه (غیرفعال کردن HTTPS اجباری)
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

# فعال‌سازی Debug Toolbar در محیط توسعه
if "debug_toolbar" not in INSTALLED_APPS:
    INSTALLED_APPS.append("debug_toolbar")

if "debug_toolbar.middleware.DebugToolbarMiddleware" not in MIDDLEWARE:
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# تنظیمات دیتابیس (در محیط توسعه معمولاً از SQLite استفاده می‌شود)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# مسیرهای داخلی برای Debug Toolbar
INTERNAL_IPS = ["127.0.0.1"]

# تنظیمات استاتیک و مدیا در محیط توسعه
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'statics']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'
