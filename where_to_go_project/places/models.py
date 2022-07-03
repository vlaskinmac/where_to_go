from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=250, verbose_name="Place")
    image = models.ForeignKey("Image",  null=True, on_delete=models.SET_NULL, related_name='images')
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return f"{self.title} {self.description_short} {self.description_long}"


class Image(models.Model):
    title = models.CharField(max_length=250, verbose_name="image")
    image = models.ImageField(null=True)
    id_image = models.AutoField(primary_key=True, verbose_name="ID")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ('pk',)