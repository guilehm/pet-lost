from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(
        _('staff'),
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )

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

    username = models.CharField(max_length=128, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
