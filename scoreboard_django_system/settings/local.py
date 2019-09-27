import os
from dotenv import load_dotenv
load_dotenv('.env.development')
from scoreboard_django_system.settings.base import *

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('APP_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DB_NAME', 'db.sqlite'),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', None),
        'PORT': os.environ.get('DB_PORT', None),
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

LOGGING_DIR = os.path.join(BASE_DIR, 'logs')
LOGGING_LEVEL = 'DEBUG'

ConfigureLogger(log_level=LOGGING_LEVEL, logging_dir=LOGGING_DIR, django_modules=PROJECT_APPS)

INSTALLED_APPS += [
    'debug_toolbar',
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

PROTECTED_ROOT = os.path.join(MEDIA_ROOT, PROTECTED_FOLDER)
PROTECTED_URL = os.path.join(MEDIA_URL, PROTECTED_FOLDER)

# DISABLE SENTRY
RAVEN_CONFIG['dsn'] = ''
RAVEN_CONFIG['environment'] = 'local'

ENABLE_MX_CHECK = False

RATE_MESSAGES_MINUTES = 5

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

RECAPTCHA_PUBLIC_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
RECAPTCHA_PRIVATE_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
