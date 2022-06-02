import logging
import bleach
from bleach.css_sanitizer import CSSSanitizer
from django.conf import settings

logger = logging.getLogger(__name__)


def clean_html(text: str) -> str:
    css_sanitizer = CSSSanitizer(allowed_css_properties=settings.BLEACH_ALLOWED_STYLES)
    new_text = bleach.clean(
        text=text,
        tags=settings.BLEACH_ALLOWED_TAGS,
        attributes=settings.BLEACH_ALLOWED_ATTRIBUTES,
        css_sanitizer=css_sanitizer,
        protocols=settings.BLEACH_ALLOWED_PROTOCOLS,
        strip=True,
    )

    return new_text
