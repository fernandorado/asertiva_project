from django.db import models
from django.core.validators import RegexValidator

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel, MultiFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.documents.edit_handlers import DocumentChooserPanel

from portfolio.models import PortfolioItem
from portfolio.models import PortfolioImages
from portfolio.models import CoverVideo
from blog.models import BlogPost


class HomePage(Page):
    """Home page model"""
    template = "index/index.html"
    max_count = 1

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('main_image', max_num=1, min_num=1),
        ], heading='Imagen de Fondo Principal Resolucion Recomendada 1900px X 1432px'),
        MultiFieldPanel([
            InlinePanel('logo_image', max_num=9, min_num=0),
        ], heading='Seccion Logos clientes, formato PNG y resolucion de 360px X 160px. Maximo de 9 logos.'),
        MultiFieldPanel([
            InlinePanel('client_image', max_num=6, min_num=0),
        ], heading='Seccion opiniones de los clientes. Maximo 6 opiniones.'),
        MultiFieldPanel([
            InlinePanel('services', max_num=6, min_num=0),
        ], heading='Seccion servicios ofrecidos. Maximo de 6 servicios.'),
        MultiFieldPanel([
            InlinePanel('contact', max_num=1, min_num=0),
        ], heading='Seccion datos de contacto.'),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['items'] = PortfolioItem.objects.live().public().order_by('-first_published_at')[:3]
        context['images'] = PortfolioImages.objects.all().order_by('-id')[:3]
        context['videos'] = CoverVideo.objects.all().order_by('-id')[:3]
        context['about'] = Nosotros.objects.all()
        context['services'] = Servicios.objects.all()
        context['blog'] = BlogPost.objects.all().order_by('-id')[:4]
        context['contact'] = ContactUs.objects.all()
        return context


class ImageHome(Orderable):
    page = ParentalKey("home.HomePage", related_name="main_image")
    imagen_fondo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    titulo_principal = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    subtitulo = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    panels = [
        ImageChooserPanel('imagen_fondo'),
        FieldPanel('titulo_principal'),
        FieldPanel('subtitulo'),
    ]


class LogoClientes(Orderable):
    """Logos Clientes para carousel"""

    page = ParentalKey("home.HomePage", related_name="logo_image")
    logo_cliente = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('logo_cliente'),
    ]


class Nosotros(Page):
    """Modelo para la seccion del Nosotros en el index"""

    max_count = 1

    titulo_nosotros = models.CharField(
        max_length=40,
        blank=False,
        null=False
    )

    subtitulo_nosotros = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    texto_nosotros = RichTextField(
        blank=True,
        max_length=1500,
        features=['bold', 'italic'],
        help_text='Escribe aqui el texto para la seccion de nosotros. Maximo 1500 caracteres'
    )

    folleto = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Subir un documento en formato pdf'
    )

    nosotros_imagen = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Resolucion optima 800px X 820px '
    )

    content_panels = Page.content_panels + [
        FieldPanel('titulo_nosotros'),
        FieldPanel('subtitulo_nosotros'),
        FieldPanel('texto_nosotros'),
        DocumentChooserPanel('folleto'),
        ImageChooserPanel('nosotros_imagen'),
    ]


class ClienteOpinion(Orderable):
    """Modelo para la seccion de clientes y sus comentarios"""

    page = ParentalKey("home.HomePage", related_name="client_image")

    imagen_cliente = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Resolucion optima 600px X 600px'
    )

    opnion_cliente = RichTextField(
        blank=False,
        max_length=600,
        features=['bold', 'italic'],
        help_text='Escribe aqui una breve opinion de tu cliente. Maximo 600 caracteres'
    )

    nombre_cliente = models.CharField(
        max_length=40,
        blank=False,
        null=False,
        help_text='Nombre del cliente o empresa. Maximo 40 caracteres.'
    )

    trabajo_realizado = models.CharField(
        max_length=40,
        blank=False,
        null=False,
        help_text='Trabajo que se le realizo al cliente'
    )

    panels = [
        ImageChooserPanel('imagen_cliente'),
        FieldPanel('opnion_cliente'),
        FieldPanel('nombre_cliente'),
        FieldPanel('trabajo_realizado'),
    ]


class Servicios(Orderable):
    """Modelo para servicios ofrecidos."""

    page = ParentalKey("home.HomePage", related_name="services")

    icono_servicio = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Usar formato PNG una resolucio de 45px X 45px.'
    )

    titulo_servicio = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        help_text='Titulo del servicio. Maximo de 30 caracteres'
    )

    resumen_servicio = models.CharField(
        blank=False,
        max_length=100,
        help_text='Breve descripcion de su servicio. Maximo de 100 caracteres.'
    )

    panels = [
        ImageChooserPanel('icono_servicio'),
        FieldPanel('titulo_servicio'),
        FieldPanel('resumen_servicio'),
    ]


class ContactUs(Orderable):
    """Modelo para la seccion de contacto en el index"""

    page = ParentalKey("home.HomePage", related_name="contact")

    correo_electronico = models.EmailField(
        blank=False,
        null=False,
        help_text="Escribe aqui el correo electronico de contacto"
    )

    numero_contacto = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        validators=[RegexValidator(r'^\d{1,10}$')],
        help_text='Numero de contacto. Direcciona hacia WhatsApp'
    )

    ubicacion = models.CharField(
        blank=True,
        max_length=100,
        help_text='Ubicacion de su empresa. Maximo de 100 caracteres.'
    )

    panels = [
        FieldPanel('correo_electronico'),
        FieldPanel('numero_contacto'),
        FieldPanel('ubicacion'),
    ]
