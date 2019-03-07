from django.contrib import admin

from announcement.models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('pet', 'active', 'situation', 'rescued', 'last_seen_city')
    list_filter = (
        'active',
        'situation',
        'rescued',
        'rescued_date',
        'lost_date',
        'found_date',
        ('last_seen_city', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ('description', 'last_seen_district', 'last_seen_detail')
    raw_id_fields = ('last_seen_city',)
