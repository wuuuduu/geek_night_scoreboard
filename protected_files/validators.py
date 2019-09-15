import os
import logging

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.text import format_lazy
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)

ALLOWED_CONTENT_TYPES = [
    'application/pdf',
    'image/png',
    'image/jpeg',
    'image/gif',
    'text/csv',
    'text/plain',
]

ALLOWED_EXTENSTIONS = [
    '.pdf',
    '.jpeg',
    '.jpg',
    '.gif',
    '.png',
    '.csv',
    '.txt'
]


def validate_file_size_and_content_type(value, *args, **kwargs):
    if value.name and not value.file:
        return value

    filesize = value.size
    file_extension = os.path.splitext(value.name)[1]
    content_type = value.content_type if getattr(value, 'content_type', None) else value.file.content_type

    if filesize > settings.MAXIMUM_FILE_SIZE:
        raise ValidationError(format_lazy('{message} 5MB', message=_('The maximum file size that can be uploaded is:')))
    elif content_type not in ALLOWED_CONTENT_TYPES:
        raise ValidationError(_('Wrong content type'))
    elif file_extension not in ALLOWED_EXTENSTIONS:
        raise ValidationError(_('Wrong extension'))
    else:
        if getattr(value, 'instance', None):
            from protected_files.models import FileContentTypes
            obj, created = FileContentTypes.objects.get_or_create(content_type=content_type)
            value.instance.content_type = obj
        return value
