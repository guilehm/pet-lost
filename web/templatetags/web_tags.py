from django import template

from web.models import Banner

register = template.Library()

translation_dict = {
    'Male': 'Macho',
    'Female': 'Fêmea',
    'Not Identified': 'Não Identificado',
}


@register.filter(name='translation')
def translation(value):
    return translation_dict.get(str(value), '')


@register.inclusion_tag('web/tags/home_slider.html')
def banners():
    active_banners = Banner.objects.filter(active=True)
    return {'banners': active_banners}
