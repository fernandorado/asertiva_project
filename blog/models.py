from django.db import models

from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField


class BlogPost(Page):
    """Modelo para la pagina del blog"""

    template = "blog/blog_page.html"
    max_count = 15

    titulo_blog = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        help_text='Titulo principal. Maximo 30 caracteres. '
    )

    fecha_publicacion = models.DateField(
        blank=False,
        null=False,
        help_text='Fecha de publicacion del post.'
    )

    autor = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text='Nombre del autor. -Opcional '
    )

    contenido_blog = RichTextField(
        blank=True,
        max_length=5000,
        features=['bold', 'italic', 'h3', 'h2', 'image', 'link'],
        help_text='Escriba aqui el contenido de su post. Maximo 5000 caracteres.'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('fondo_blog', max_num=1, min_num=1, label='Imagen Fondo del Post'),
        ], heading='Iamgen de fondo para el Post, resolucion optima 1280px X 847px'),
        MultiFieldPanel([
            FieldPanel('titulo_blog'),
            FieldPanel('fecha_publicacion'),
            FieldPanel('autor'),
            FieldPanel('contenido_blog'),
        ], heading='Datos del Item'),

    ]


class ImagenFondoBlog(Orderable):
    """ Imagen de fondo para el blog"""

    page = ParentalKey("BlogPost", related_name="fondo_blog")
    imagen_blog = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel("imagen_blog"),
    ]
