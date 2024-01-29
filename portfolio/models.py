from django.db import models

from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField


class PortfolioItem(Page):
    """Template for each item in portfolio"""

    template = "portfolio/portfolio_item.html"

    titulo_principal = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        help_text='Titulo principal. Maximo 30 caracteres. '
    )

    fecha_proyecto = models.DateField(
        blank=True,
        null=True,
        help_text='Fecha de incio o terminacion del Proyecto'
    )

    funciones_cargo = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        help_text='Funciones del Cargo. Ej: Diseño, Edicion Video, Grabacion. Maximo 30 caracteres.'
    )

    cliente = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        help_text='Nombre del Cliente. Maximo 20 caracteres.'
    )

    web_cliente = models.URLField(
        blank=True,
        null=True,
        help_text='Si el cliente posee sitio web la URL va aqui'

    )

    descripcion = RichTextField(
        blank=True,
        max_length=1500,
        features=['bold', 'italic'],
        help_text='Describa aqui el proyecto y sus labores. Maximo 1500 caracteres'
    )

    def main_image(self):
        gallery_item = self.imagenes_portfolio.first()
        if gallery_item:
            return gallery_item.imagen_portfolio
        else:
            return None

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('titulo_principal'),
            FieldPanel('fecha_proyecto'),
            FieldPanel('funciones_cargo'),
            FieldPanel('cliente'),
            FieldPanel('web_cliente'),
            FieldPanel('descripcion'),
        ], heading='Datos del Item'),
        MultiFieldPanel([
            InlinePanel('imagenes_portfolio', max_num=6, min_num=1, label='Publicar Post en Portafolio'),
        ], heading='Fotos para el Post, resolucion optima 1280px X 847px'),
    ]


class ImagenesPorfolio(Orderable):
    """ Imagenes del porfolio entre 1 y 6."""

    page = ParentalKey("PortfolioItem", related_name="imagenes_portfolio")
    imagen_portfolio = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel("imagen_portfolio"),
    ]


class PublicarImagen(Page):
    """Imagenes para publicar en el portafolio pagina principal"""

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('imagen_portafolio', max_num=1, min_num=1, label='Publicar Imagen'),
        ], heading='Foto unica para el portafolio, resolucion optima 900px X 760px'),
    ]


class PortfolioImages(Orderable):
    """ Imagen unica para Portafolio"""

    page = ParentalKey("PublicarImagen", related_name="imagen_portafolio")
    imagen_post = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    titulo_imagen = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        help_text='Titulo opcional de la imagen. Maximo 100 caracteres'
    )
    subtitulo_imagen = models.CharField(
        blank=True,
        null=True,
        max_length=75,
        help_text='Subtitulo opcional de la imagen. Maximo 75 caracteres'
    )

    panels = [
        ImageChooserPanel("imagen_post"),
        FieldPanel('titulo_imagen'),
        FieldPanel('subtitulo_imagen'),
    ]


class PublicarVideo(Page):
    """Modelo para crear una publicacion de video en el index"""

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('covers_video', max_num=1, min_num=1, label='Publicacion de  Video'),
        ], heading='Cover o imagen para el video en el index, resolucion optima 900px X 760px'),
    ]


class CoverVideo(Orderable):
    """ Cover para el video en el index """

    page = ParentalKey("PublicarVideo", related_name="covers_video")

    url_video = models.URLField(
        blank=False,
        help_text='Inserte aqui la url del video'
    )

    cover_video = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    titulo_video = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        help_text='Titulo opcional de la imagen. Maximo 100 caracteres'
    )
    subtitulo_video = models.CharField(
        blank=True,
        null=True,
        max_length=75,
        help_text='Subtitulo opcional de la imagen. Maximo 75 caracteres'
    )

    panels = [
        FieldPanel('url_video'),
        ImageChooserPanel('cover_video'),
        FieldPanel('titulo_video'),
        FieldPanel('subtitulo_video'),
    ]
