from .base import *
import os
print('DEBUG FROM ENV:', os.getenv('DEBUG'))
DEBUG = os.getenv("DEBUG", "False").lower() == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "example.com").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "mydb_prod"),
        "USER": os.getenv("POSTGRES_USER", "myuser_prod"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "mypassword_prod"),
        "HOST": os.getenv("POSTGRES_HOST", "prod-db-server"),
        "PORT": os.getenv("POSTGRES_PORT", 5432),
    }
}

CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 3600