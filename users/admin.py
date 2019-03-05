from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
                'phone_number',
                'mobile_phone_number',
                'org_name',
                'profile_picture',
            )
        }),
        (_('Address Data'), {
            'fields': (
                'postal_code',
                'address',
                'number',
                'complement',
                'district',
                'city',
            )
        }),
        (_('Social Media'), {
            'fields': (
                'url_facebook_profile',
                'url_facebook_page',
                'url_twitter',
                'url_instagram',
            )
        }),
        (_('Permissions'), {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'share_email',
            'share_phone',
            'groups',
            'user_permissions',
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-id',)
    list_filter = ('is_superuser', 'is_active', 'share_email', 'share_phone')
    raw_id_fields = ('city',)
    readonly_fields = ('date_joined',)
