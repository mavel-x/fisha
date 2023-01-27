from django.db import models


class Place(models.Model):
    title = models.CharField('название', max_length=200)
    description_short = models.TextField('краткое описание')
    description_long = models.TextField('длинное описание')
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='место',
                              related_name='images', related_query_name='image')
    image = models.ImageField('картинка')

    def __str__(self):
        return f'{self.id}: {self.place.title}'
