import logging
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from ordered_model.models import OrderedModel

from pages.helpers import clean_html

logger = logging.getLogger(__name__)


class CMSPage(models.Model):
    slug = models.CharField(
        max_length=120,
        unique=True,
        blank=False,
        null=False,
        help_text=_('The public url to the page, example: https://website.com/YOUR_SLUG_HERE/')
    )

    public_content = models.TextField(
        max_length=40000,
        blank=True,
        null=False
    )

    visible = models.BooleanField(
        default=True,
        null=False
    )

    def save(self, **kwargs):
        self.public_content = clean_html(self.public_content)
        return super(CMSPage, self).save(**kwargs)

    def __str__(self):
        on_or_off = 'online' if self.visible else 'offline'
        return f'Page: /{self.slug}/ - {on_or_off}'


class SponsorsCarousel(OrderedModel):
    image = models.ImageField(upload_to='sponsors/', null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=True)
    visible = models.BooleanField(null=False, default=True)

    def __str__(self):
        return str(self.image)
