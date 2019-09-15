import logging.config
import os
from typing import List

from django.utils.log import DEFAULT_LOGGING

# Disable Django's logging setup
LOGGING_CONFIG = None


class ConfigureLogger:
    def __init__(self, log_level: str, logging_dir: str, django_modules: List[str]):
        """
        Configure logging for all apps and common files in django app
        """
        # TODO: Autodiscovery files in module :)
        files = [
            'models',
            'admin',
            'tasks',
            'tests',
            'urls',
            'views',
            'api_views',
            'helpers',
            'forms',
        ]

        log_level = log_level.upper()
        logger_config = {
            'version': 1,
            'disable_existing_loggers': False,
            'filters': {
                'require_debug_false': {
                    '()': 'django.utils.log.RequireDebugFalse',
                },
                'require_debug_true': {
                    '()': 'django.utils.log.RequireDebugTrue',
                },
            },
            'formatters': {
                'default': {
                    # exact format is not important, this is the minimum information
                    # 'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    'format': '%(levelname)s %(asctime)s %(name)s.%(funcName)s:%(lineno)s: %(message)s'
                },
                'django.server': DEFAULT_LOGGING['formatters']['django.server'],
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'filters': ['require_debug_true'],
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                },
                'sentry': {
                    'level': 'ERROR',
                    'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                },
                'root': {
                    'level': 'DEBUG',
                    'class': 'logging.FileHandler',
                    'formatter': 'default',
                    'filename': os.path.join(logging_dir, 'root.log'),
                },
                'django.server': DEFAULT_LOGGING['handlers']['django.server'],
            },
            'loggers': {
                # default for all undefined Python modules
                '': {
                    'level': 'WARNING',
                    'handlers': ['console', 'root', 'sentry'],
                },
                # Default runserver request logging
                'django.server': DEFAULT_LOGGING['loggers']['django.server'],
            },
        }
        for django_module in django_modules:
            logger_config['handlers'][django_module] = {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': os.path.join(logging_dir, '{}.log'.format(django_module)),
            }
            logger_config['loggers'][django_module] = {
                'level': log_level,
                'handlers': ['console', django_module, 'sentry'],
                # Avoid double logging because of root logger
                'propagate': False,
            }
            for file in files:
                tmp = '{}.{}'.format(django_module, file)
                logger_config['handlers'][tmp] = {
                    'level': 'DEBUG',
                    'class': 'logging.FileHandler',
                    'formatter': 'default',
                    'filename': os.path.join(logging_dir, '{}.log'.format(tmp)),
                }
                logger_config['loggers'][tmp] = {
                    'level': log_level,
                    'handlers': ['console', tmp, 'sentry'],
                    # Avoid double logging because of root logger
                    'propagate': False,
                }

        logging.config.dictConfig(logger_config)
