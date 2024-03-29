from django import template

from ..models import Footer

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    return Footer.objects.get(slug=slug)
