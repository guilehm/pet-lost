from django.shortcuts import render
from pet.models import Pet


def index(request):
    lost = Pet.objects.filter(
        situation=Pet.SITUATION_LOST,
        rescued=False,
    ).order_by('?').select_related('picture')[:4]
    found = Pet.objects.filter(
        situation=Pet.SITUATION_FOUND,
        rescued=False,
    ).order_by('?').select_related('picture')[:4]
    return render(request, 'web/index.html', {
        'lost': lost,
        'found': found,
    })
