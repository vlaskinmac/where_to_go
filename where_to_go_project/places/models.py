from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=250, null=True, blank=True)
    description_short = models.CharField(max_length=250)
    description_long = models.CharField(max_length=250)
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f"{self.title} {self.description_short} {self.description_long}"