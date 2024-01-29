from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    """Social media para el footer """

    facebook = models.URLField(blank=True, null=True, help_text='Pagina de Facebook')
    instagram = models.URLField(blank=True, null=True, help_text='Perfil de Instagram')
    whatsapp = models.BigIntegerField(blank=True, null=True, help_text='Numero de WhatsApp')

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("instagram"),
            FieldPanel("whatsapp"),
        ], heading='Redes Sociales y Comunicacion')
    ]
