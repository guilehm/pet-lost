from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Announcement(models.Model):
    SITUATION_LOST = 'lost'
    SITUATION_FOUND = 'found'
    SITUATION_CHOICES = (
        (SITUATION_LOST, 'Lost'),
        (SITUATION_FOUND, 'Found'),
    )

    active = models.BooleanField(default=True)
    pet = models.ForeignKey(
        'pet.Pet',
        related_name='announcements',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'users.User',
        related_name='announcements',
        on_delete=models.CASCADE,
    )
    situation = models.CharField(max_length=128, choices=SITUATION_CHOICES)
    message = models.TextField()

    rescued = models.BooleanField(default=False)
    rescued_date = models.DateField(null=True, blank=True)

    last_seen_district = models.CharField(max_length=512)
    last_seen_city = models.ForeignKey(
        'location.City', related_name='pets', db_index=True, on_delete=models.CASCADE
    )
    last_seen_detail = models.CharField(max_length=512)

    lost_date = models.DateField(db_index=True, null=True, blank=True)
    found_date = models.DateField(db_index=True, null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def clean(self):
        if not any([self.lost_date, self.found_date]):
            raise ValidationError('Lost Date or Found Date must be filled')

        if self.lost_date and not self.pet.name:
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
                sex='a' if self.pet.sex == self.pet.SEX_FEMALE else 'o',
                date=self.found_date.strftime("%d/%m/%Y")
            )
            lost_description += text
        text = f'Me viram por último em {self.last_seen_city.data}, {self.last_seen_detail}\n'
        lost_description += text
        if self.pet.sex == self.pet.SEX_NOT_IDENTIFIED:
            text = 'Ainda não identificaram meu sexo.'
        elif self.pet.sex == self.pet.SEX_MALE:
            text = 'Sou um macho.'
        elif self.pet.sex == self.pet.SEX_FEMALE:
            text = 'Sou uma fêmea.'
        lost_description += f'{text}\n'
        if not self.rescued:
            text = 'Ainda não encontrei minha família, conto com sua ajuda para encontrá-los.'
        else:
            text = f'Fui recuperado por minha família em ' \
                f'{self.rescued_date.strftime("%d/%m/%Y")} graças à ajuda de pessoas como você.'
        lost_description += text
        return lost_description