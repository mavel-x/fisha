from django.db import models
from django.utils.html import format_html

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('название', max_length=200)
    description_short = models.TextField('краткое описание')
    description_long = HTMLField('длинное описание')
    lat = models.FloatField('широта')
    lng = models.FloatField('долгота')
    slug = models.SlugField('слаг', unique=True)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='место',
                              related_name='images', related_query_name='image')
    image = models.ImageField('картинка')
    position = models.PositiveIntegerField('порядковый номер', default=0, null=True, blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position}: {self.place.title}'

    def preview(self):
        return format_html('<img src="{url}" height={height} />'.format(
            url=self.image.url,
            height=min(self.image.height, 200),
        )
        )
