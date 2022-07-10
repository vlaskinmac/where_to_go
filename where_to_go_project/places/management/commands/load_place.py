from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Получить локацию с картинками'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, nargs='+')

    def handle(self, *args, **options):
        try:
            for location in options['json_url']:
                location_response = requests.get(location)
                location_response.raise_for_status()
                location = location_response.json()
                image_links = location['imgs']
                place, is_created = Place.objects.get_or_create(
                    title=location['title'],
                    lng=location['coordinates']['lng'],
                    lat=location['coordinates']['lat'],
                    defaults={
                        'description_short': location['description_short'],
                        'description_long': location['description_long'],
                    }
                )
                if not is_created:
                    place.imges.all().delete()

                for index, img_link in enumerate(image_links):
                    try:
                        filename = unquote(Path(urlparse(img_link).path).name)
                        image_response = requests.get(img_link)
                        image_response.raise_for_status()
                        image_content = ContentFile(image_response.content)

                        place_image = PlaceImage(id_image=index, place=place)
                        place_image.image.save(filename, content=image_content)
                    except requests.exceptions.HTTPError:
                        self.stderr.write(self.style.ERROR(
                            f'Картинка {img_link} не найдена'))
                self.stdout.write(self.style.SUCCESS('Локация загружена!'))
        except requests.exceptions.HTTPError:
            self.stderr.write(self.style.ERROR(
                f'Описание локации {options["json_url"]} недоступно'))
        except KeyError as exc:
            self.stderr.write(self.style.ERROR(
                f'В описании локации не найдено поле "{exc.args[0]}"'))