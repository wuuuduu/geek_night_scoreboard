from debug_toolbar.settings import PANELS_DEFAULTS

from .base import *

DEBUG = True

X_FRAME_OPTIONS = "SAMEORIGIN"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DEBUG_TOOLBAR_CONFIG = {"SHOW_COLLAPSED": True, "SHOW_TOOLBAR_CALLBACK": lambda x: True}
DEBUG_TOOLBAR_PANELS = PANELS_DEFAULTS + [
    "cachalot.panels.CachalotPanel",
]

# DISABLE SENTRY
RAVEN_CONFIG["dsn"] = ""
RAVEN_CONFIG["environment"] = "local"

ENABLE_MX_CHECK = False

RATE_MESSAGES_MINUTES = 5

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
