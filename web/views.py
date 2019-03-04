from django.shortcuts import render
from pet.models import Pet


def index(request):
    lost = Pet.objects.filter(
        situation=Pet.SITUATION_LOST,
        rescued=False,
    ).select_related('picture')
    found = Pet.objects.filter(
        situation=Pet.SITUATION_FOUND,
        rescued=False,
    ).select_related('picture')
    return render(request, 'web/index.html', {
        'lost': lost,
        'found': found,
    })
