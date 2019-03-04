from django.contrib import admin

from web.models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'subtitle', 'slug')
    list_filter = ('active', 'date_added', 'date_changed')
    prepopulated_fields = {'slug': ('title',)}
