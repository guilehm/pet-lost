import uuid

from django.core.exceptions import ValidationError
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

    SITUATION_LOST = 'lost'
    SITUATION_FOUND = 'found'
    SITUATION_CHOICES = (
        (SITUATION_LOST, 'Lost'),
        (SITUATION_FOUND, 'Found'),
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
    kind = models.CharField(max_length=128, choices=TYPE_CHOICES, default=TYPE_DOG)
    slug = models.SlugField(db_index=True, unique=True)
    breed = models.ForeignKey('pet.Breed', on_delete=models.CASCADE, null=True)
    situation = models.CharField(max_length=128, choices=SITUATION_CHOICES, default=SITUATION_LOST)
    lost_date = models.DateField(db_index=True, null=True, blank=True)
    found_date = models.DateField(db_index=True, null=True, blank=True)
    rescued = models.BooleanField(default=False)
    rescued_date = models.DateField(null=True, blank=True)
    picture = models.ForeignKey('pet.Picture', null=True, blank=True, on_delete=models.SET_NULL)
    pictures = models.ManyToManyField('pet.Picture', related_name='pets', blank=True)
    description = models.TextField(null=True, blank=True)
    location_city = models.ForeignKey('location.City', db_index=True, on_delete=models.CASCADE)
    location_detail = models.CharField(max_length=512)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.kind} #{str(self.id)[:8]} ({self.name})'

    def clean(self):
        if not any([self.lost_date, self.found_date]):
            raise ValidationError('Lost Date or Found Date must be filled')

        if self.lost_date and not self.name:
            raise ValidationError('Please fill the name of your pet')

        if not self.situation:
            if self.found_date:
                self.situation = self.SITUATION_FOUND
            elif self.lost_date:
                self.situation = self.SITUATION_LOST

        if self.rescued and not self.rescued_date:
            self.rescued_date = timezone.now()

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    @property
    def lost_description(self):
        lost_description = ''
        if self.situation == self.SITUATION_LOST:
            text = f'Eu desapareci no dia {self.lost_date.strftime("%d/%m/%Y")}.\n'
            lost_description += text
        elif self.situation == self.SITUATION_FOUND:
            text = 'Fui encontrad{sex} no dia {date}.\n'.format(
                sex='a' if self.sex == self.SEX_FEMALE else 'o',
                date=self.found_date.strftime("%d/%m/%Y")
            )
            lost_description += text
        text = f'Me viram por último em {self.location_city.data}, {self.location_detail}\n'
        lost_description += text
        if self.sex == self.SEX_NOT_IDENTIFIED:
            text = 'Ainda não identificaram meu sexo.'
        elif self.sex == self.SEX_MALE:
            text = 'Sou um macho.'
        elif self.sex == self.SEX_FEMALE:
            text = 'Sou uma fêmea.'
        lost_description += f'{text}\n'
        if not self.rescued:
            text = 'Ainda não encontrei minha família, conto com sua ajuda para encontrá-los.'
        else:
            text = f'Fui recuperado por minha família em ' \
                f'{self.rescued_date.strftime("%d/%m/%Y")} graças à ajuda de pessoas como você.'
        lost_description += text
        return lost_description


class Picture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=512, null=True, blank=True)
    image = models.ImageField(upload_to='pet/picture/image')

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return '#{id}{title}'.format(
            id=self.id,
            title=f' ({self.title})' if self.title else '',
        )

    class Meta:
        ordering = ('date_changed', )
