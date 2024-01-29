"""Menus models."""

from django.db import models

from django_extensions.db.fields import AutoSlugField  # install django-extensions
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class FooterMenu(Orderable):
    """Modelo para el footer links social media"""

    page = ParentalKey('Footer', related_name="footer_items")

    titulo_link = models.CharField(
        blank=False,
        null=True,
        max_length=50
    )
    url_sitio = models.CharField(
        max_length=500,
        blank=True
    )

    abrir_en_nueva_ventana = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel('titulo_link'),
        FieldPanel('url_sitio'),
        FieldPanel('abrir_en_nueva_ventana'),
    ]


@register_snippet
class Footer(ClusterableModel):
    """The main menu"""

    titulo = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='titulo', editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('titulo'),
            FieldPanel('slug'),
        ], heading='Social Media para el Footer'),
        InlinePanel('footer_items', label='Footer links')
    ]

    def __str__(self):
        return self.titulo
