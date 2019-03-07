from django.db import models

from web.utils import UploadToFactory


class Banner(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    subtitle = models.CharField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    active = models.BooleanField(default=True)
    picture = models.ImageField(
        null=True,
        blank=True,
        upload_to=UploadToFactory('web/banner/picture'),
    )
    button_one = models.CharField(max_length=32, null=True, blank=True)
    button_two = models.CharField(max_length=32, null=True, blank=True)
    button_one_link = models.URLField(null=True, blank=True)
    button_two_link = models.URLField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return '#{id}{title}'.format(
            id=self.id,
            title=f' ({self.title})' if self.title else '',
        )

    class Meta:
        ordering = ('date_changed', )
