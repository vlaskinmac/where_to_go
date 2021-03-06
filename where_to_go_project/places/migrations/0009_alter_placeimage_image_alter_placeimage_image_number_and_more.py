# Generated by Django 4.0.6 on 2022-07-14 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_placeimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image_number',
            field=models.PositiveSmallIntegerField(db_index=True, verbose_name='Номер изображения'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imges', to='places.place', verbose_name='Изображения'),
        ),
    ]
