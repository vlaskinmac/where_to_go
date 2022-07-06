from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    description_short = models.TextField(
        blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(
        blank=True, verbose_name='Полное описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название проекта")
    image = models.ImageField(blank=True, null=True)
    id_image = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        default=0,
        db_index=True
    )

    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='imges'
    )

    def __str__(self):
        return f'{self.id_image} {self.place.title}'

    class Meta:
        ordering = ['id_image']