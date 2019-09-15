import logging
import bleach
from django.conf import settings

logger = logging.getLogger(__name__)


def clean_html(text: str) -> str:
    new_text = bleach.clean(
        text=text,
        tags=settings.BLECH_ALLOWED_TAGS,
        attributes=settings.BLECH_ALLOWED_ATTRIBUTES,
        styles=settings.BLECH_ALLOWED_STYLES,
        protocols=settings.BLECH_ALLOWED_PROTOCOLS,
        strip=True,
    )

    return new_text
