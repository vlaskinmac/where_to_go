# Generated by Django 4.0.6 on 2022-07-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_placeimage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='image_number',
            field=models.PositiveSmallIntegerField(db_index=True),
        ),
    ]
