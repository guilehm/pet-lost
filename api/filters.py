from django_filters import FilterSet, ModelChoiceFilter

from location.models import City


class AnnouncementFilterSet(FilterSet):
    lastSeenCity = ModelChoiceFilter(
        queryset=City.objects.all(),
        field_name='last_seen_city',
        to_field_name='name',
        label='Last Seen City',
    )
