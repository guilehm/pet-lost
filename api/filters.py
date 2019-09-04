from django_filters import FilterSet, ModelChoiceFilter, DateFilter, CharFilter

from location.models import City
from pet.models import Breed


class AnnouncementFilterSet(FilterSet):
    lastSeenCity = ModelChoiceFilter(
        queryset=City.objects.all(),
        field_name='last_seen_city',
        to_field_name='name',
        label='Last Seen City',
    )
    rescuedDate = DateFilter(
        field_name='rescued_date',
        label='Rescued Date',
    )
    lostDate = DateFilter(
        field_name='lost_date',
        label='Lost Date',
    )
    foundDate = DateFilter(
        field_name='found_date',
        label='Found Date',
    )


class PetFilterSet(FilterSet):
    breed = ModelChoiceFilter(
        queryset=Breed.objects.all(),
        field_name='breed',
        to_field_name='name',
        label='Breed',
    )
    name = CharFilter()
    sex = CharFilter()
    kind = CharFilter()
    slug = CharFilter()
    description = CharFilter()
