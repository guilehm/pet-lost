import uuid

from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify

from announcement.models import Announcement
from web.utils import UploadToFactory


class BreedQuerySet(models.QuerySet):
    def active(self):
        return self.filter(
            pets__isnull=False,
        )


class PetQuerySet(models.QuerySet):
    def lost(self):
        return self.filter(
            announcements__rescued=False,
            announcements__active=True,
            announcements__situation=Announcement.SITUATION_LOST,
        ).distinct()

    def found(self):
        return self.filter(
            announcements__rescued=False,
            announcements__active=True,
            announcements__situation=Announcement.SITUATION_FOUND,
        ).distinct()

    def rescued(self):
        return self.filter(
            announcements__rescued=True,
        ).distinct()

    def active(self):
        return self.filter(
            announcements__active=True,
        ).distinct()


class Breed(models.Model):
    TYPE_DOG = 'dog'
    TYPE_CHOICES = (
        (TYPE_DOG, 'Dog'),
    )
    name = models.CharField(max_length=128)
    kind = models.CharField(max_length=128, choices=TYPE_CHOICES, default=TYPE_DOG)
    slug = models.SlugField(db_index=True, unique=True)
    description = models.TextField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    objects = BreedQuerySet.as_manager()

    def __str__(self):
        return f'{self.name}'


class Pet(models.Model):
    KIND_DOG = 'dog'
    KIND_CHOICES = (
        (KIND_DOG, 'Dog'),
    )

    SEX_MALE = 'male'
    SEX_FEMALE = 'female'
    SEX_NOT_IDENTIFIED = 'not_identified'
    SEX_CHOICES = (
        (SEX_MALE, 'Male'),
        (SEX_FEMALE, 'Female'),
        (SEX_NOT_IDENTIFIED, 'Not Identified'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        'users.User',
        related_name='pets',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=128, null=True, blank=True)
    sex = models.CharField(max_length=32, choices=SEX_CHOICES)
    kind = models.CharField(max_length=128, choices=KIND_CHOICES, default=KIND_DOG)
    slug = models.SlugField(db_index=True, unique=True)
    breed = models.ForeignKey(
        'pet.Breed', related_name='pets', on_delete=models.CASCADE, null=True
    )
    picture = models.ForeignKey(
        'pet.Picture', null=True, blank=True, on_delete=models.SET_NULL
    )
    pictures = models.ManyToManyField('pet.Picture', related_name='pets', blank=True)
    description = models.TextField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    objects = PetQuerySet.as_manager()

    def __str__(self):
        return f'{self.kind} #{str(self.id)[:8]} ({self.name})'

    @cached_property
    def announcement(self):
        return self.announcements.filter(active=True).last()

    @property
    def public_id(self):
        text = "{pet_name}-{kind}-{breed}-{id}".format(
            pet_name=self.name,
            kind=self.kind,
            breed=self.breed.name,
            id=str(self.id)[:5],
        )
        return slugify(text)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.public_id
        super().save(*args, **kwargs)


class Picture(models.Model):
    original_file_name = models.CharField(max_length=1024, null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True)
    image = models.ImageField(upload_to=UploadToFactory('pet/picture/image'))

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return '#{id}{title}'.format(
            id=self.id,
            title=f' ({self.title})' if self.title else '',
        )

    class Meta:
        ordering = ('date_changed', )
