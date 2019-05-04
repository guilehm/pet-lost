from django.contrib import admin

from announcement.models import Announcement, Comment


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
    search_fields = ('description', 'last_seen_district')
    raw_id_fields = ('last_seen_city',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'announcement',
        'user',
        'deleted',
    )
    list_filter = (
        'announcement',
        'user',
        'deleted',
        'date_added',
        'date_changed',
    )
    search_fields = ('description',)
