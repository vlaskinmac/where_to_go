from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=250, verbose_name="Place")
    details_place = models.TextField(verbose_name="Места")
    title_place = models.CharField(max_length=250, verbose_name="Название проекта")
    placeId = models.CharField(max_length=250, verbose_name="ID проекта")

    def __str__(self):
        return f"{self.title}"


class Image(models.Model):
    title = models.CharField(max_length=250, verbose_name="image")
    image = models.ImageField()
    id_image = models.AutoField(primary_key=True, verbose_name="ID")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ('pk',)