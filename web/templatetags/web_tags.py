from django import template

from announcement.models import Announcement
from web.models import Banner

register = template.Library()

translation_dict = {
    'Name': 'Nome',
    'Sex': 'Sexo',
    'Breed': 'Raça',
    'Male': 'Macho',
    'Female': 'Fêmea',
    'Not Identified': 'Não Identificado',
    'Pet': 'Pet',
    'Active': 'Ativo',
    'Lost': 'Desaparecido',
    'Found': 'Encontrado',
    'Situation': 'Situação',
    'Description': 'Descrição',
    'Rescued': 'Resgatado',
    'Rescued date': 'Resgatado em',
    'Last seen district': 'Bairro',
    'Last seen city': 'Cidade',
    'Last seen detail': 'Detalhes',
    'Lost date': 'Desaparecido em',
    'Found date': 'Encontrado em',
    'Please, choose a pet': 'Por favor, escolha um pet.',
    'A pet may not have more than one active announcement': 'Um pet pode ter apenas um anúncio ativo.',
    'Lost Date or Found Date must be filled': 'Preencha a data em que o pet desapareceu ou foi encontrado.',
}


@register.filter(name='translation')
def translation(value):
    return translation_dict.get(str(value), '') or value


@register.inclusion_tag('web/tags/home_slider.html')
def banners(request):
    active_banners = Banner.objects.filter(active=True)
    return {'messages': request._messages, 'banners': active_banners}


@register.inclusion_tag('web/tags/pet_list.html', takes_context=True)
def pet_list(context, situation=None):
    if situation == Announcement.SITUATION_LOST:
        pets = context['pets_lost']
    elif situation == Announcement.SITUATION_FOUND:
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
