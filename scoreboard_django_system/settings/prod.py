from dotenv import load_dotenv

load_dotenv('.env.prod')
from .base import *
from .security_settings import *

ConfigureLogger(log_level=LOGGING_LEVEL, logging_dir=LOGGING_DIR, django_modules=PROJECT_APPS)

SECRET_KEY = os.environ.get('SECRET_KEY')

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

ALLOWED_HOSTS = [
    'scoreboard.nocinformatyka.pl'
]
RAVEN_CONFIG['dsn'] = os.environ.get('RAVEN_DSN')
RAVEN_CONFIG['environment'] = 'prod'

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')

EMAIL_USE_TLS = bool(int(os.environ.get('EMAIL_USE_TLS', 1)))
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'scoreboard@localhost')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_TIMEOUT = int(os.environ.get('EMAIL_TIMEOUT'))
