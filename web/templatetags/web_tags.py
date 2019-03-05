from django import template

from pet.models import Pet
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
def banners(request):
    active_banners = Banner.objects.filter(active=True)
    return {'messages': request._messages, 'banners': active_banners}


@register.inclusion_tag('web/tags/pet_list.html', takes_context=True)
def pet_list(context, situation=None):
    if situation == Pet.SITUATION_LOST:
        pets = context['pets_lost']
    elif situation == Pet.SITUATION_FOUND:
        pets = context['pets_found']
    else:
        pets = context['pets']
    lost = context.get('lost')
    found = context.get('found')
    return {
        'pets': pets,
        'lost': lost,
        'found': found,
    }
