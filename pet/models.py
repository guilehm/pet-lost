import uuid

from django.db import models
from django.utils import timezone


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
    TYPE_DOG = 'dog'
    TYPE_CHOICES = (
        (TYPE_DOG, 'Dog'),
    )

    STATUS_LOST = 'lost'
    STATUS_FOUND = 'found'
    STATUS_CHOICES = (
        (STATUS_LOST, 'Lost'),
        (STATUS_FOUND, 'Found'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    kind = models.CharField(max_length=128, choices=TYPE_CHOICES, default=TYPE_DOG)
    slug = models.SlugField(db_index=True, unique=True)
    breed = models.ForeignKey('pet.Breed', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=128, choices=STATUS_CHOICES, default=STATUS_LOST)
    lost_date = models.DateField(default=timezone.now)
    description = models.TextField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.kind} #{str(self.id)[:8]} ({self.name})'


class Picture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=512, null=True, blank=True)
    primary = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='pet/picture/image',
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'#{self.id} ({self.title})'

    class Meta:
        ordering = ('date_changed', )
