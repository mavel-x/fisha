from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'название',
        max_length=200,
        unique=True
    )
    description_short = models.TextField(
        'краткое описание',
        blank=True,
    )
    description_long = HTMLField(
        'длинное описание',
        blank=True,
    )
    lat = models.FloatField('широта')
    lng = models.FloatField('долгота')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='место',
        related_name='images',
    )
    image = models.ImageField('картинка')
    position = models.PositiveIntegerField(
        'порядковый номер',
        default=0
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position}: {self.place.title}'
