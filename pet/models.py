import uuid

from django.db import models
from django.utils.functional import cached_property

from announcement.models import Announcement
from web.utils import UploadToFactory


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
        return self.filter(rescued=True)


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
