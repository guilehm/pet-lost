from django_filters import FilterSet, ModelChoiceFilter, DateFilter

from location.models import City


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
