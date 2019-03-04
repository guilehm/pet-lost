from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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


def lost_list(request):
    lost_qs = Pet.objects.filter(
        situation=Pet.SITUATION_LOST,
        rescued=False,
    ).select_related('picture')

    page = request.GET.get('page')
    paginator = Paginator(lost_qs, 8)
    try:
        lost = paginator.page(page)
    except PageNotAnInteger:
        lost = paginator.page(1)
    except EmptyPage:
        lost = paginator.page(paginator.num_pages)

    return render(request, 'web/lost_found.html', {
        'pets': lost,
        'lost': True,
    })
