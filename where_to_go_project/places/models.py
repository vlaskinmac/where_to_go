from django.db import models
from tinymce.models import HTMLField


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

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название проекта")
    image = models.ImageField(blank=True, verbose_name="изображение")
    image_number = models.PositiveSmallIntegerField(
        db_index=True
    )

    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='imges'
    )

    def __str__(self):
        return f'{self.image_number} {self.place.title}'

    class Meta:
        ordering = ['image_number']
        verbose_name = 'Изображение места'
        verbose_name_plural = 'Изображение мест'