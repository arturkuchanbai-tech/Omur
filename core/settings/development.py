from .base import *
import os

DEBUG = False

DISABLE_SERVER_SIDE_CURSORS = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "omur_project",
        "USER": "omur_user",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
CORS_ALLOW_ALL_ORIGINS = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"