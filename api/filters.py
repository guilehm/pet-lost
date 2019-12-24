from django_filters import BooleanFilter, CharFilter, DateFilter, FilterSet, ModelChoiceFilter

from location.models import City
from pet.models import Breed, Pet


class AnnouncementFilterSet(FilterSet):
    pet = ModelChoiceFilter(
        queryset=Pet.objects.all(),
        field_name='pet',
        to_field_name='id',
        label='Pet',
    )
    active = BooleanFilter()
    situation = CharFilter()
    rescued = BooleanFilter()
    description = CharFilter()
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
    situation = CharFilter(
        method='filter_situation',
        label='situation',
    )
    rescued = BooleanFilter(
        method='filter_rescued',
        label='rescued pets',
    )
    active = BooleanFilter(
        method='filter_active',
        label='active pets',
    )

    def filter_situation(self, queryset, name, value):
        if value and value.lower() in ['lost', 'found']:
            return getattr(queryset, value.lower())()
        return queryset

    def filter_rescued(self, queryset, name, value):
        if value:
            return queryset.rescued()
        return queryset

    def filter_active(self, queryset, name, value):
        if value:
            return queryset.active()
        return queryset


class BreedFilterSet(FilterSet):

    active = BooleanFilter(
        method='filter_active',
        label='active breeds',
    )

    def filter_active(self, queryset, name, value):
        if value:
            return queryset.active()
        return queryset
