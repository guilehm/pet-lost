
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField(_('email address'), unique=True)

    share_email = models.BooleanField(default=False)
    share_phone = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    mobile_phone_number = models.CharField(max_length=20, null=True, blank=True)
    org_name = models.CharField(_('organization name'), max_length=128, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='users/user/profile-picture', null=True, blank=True)

    postal_code = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    complement = models.CharField(max_length=128, null=True, blank=True)
    district = models.CharField(max_length=128, null=True, blank=True)
    city = models.ForeignKey(
        'location.City',
        on_delete=models.SET_NULL,
        related_name='users',
        null=True,
        blank=True,
    )

    url_facebook_profile = models.URLField('Profile Facebook URL', null=True, blank=True)
    url_facebook_page = models.URLField('Page Facebook URL', null=True, blank=True)
    url_twitter = models.URLField('Twitter URL', null=True, blank=True)
    url_instagram = models.URLField('Instagram URL', null=True, blank=True)
