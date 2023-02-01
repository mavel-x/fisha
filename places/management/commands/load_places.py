from io import BytesIO
from pathlib import Path
from urllib.parse import urlsplit

import requests
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile

from places.models import Place


def load_place_to_db(place: dict):
    new_place, created = Place.objects.get_or_create(
        title=place['title'],
        defaults={
            'description_short': place['description_short'],
            'description_long': place['description_long'],
            'lat': place['coordinates']['lat'],
            'lng': place['coordinates']['lng'],
        }
    )
    if not created:
        return

    for position, url in enumerate(place['imgs'], start=1):
        response = requests.get(url)
        response.raise_for_status()
        filename = Path(urlsplit(url).path).name
        image_file = ImageFile(file=BytesIO(response.content), name=filename)
        new_place.images.create(image=image_file, position=position)


class Command(BaseCommand):
    help = 'Get place data from a remote JSON file and save a place to DB.'

    def add_arguments(self, parser):
        parser.add_argument('json_urls',
                            help='URL(s) of the remote file(s) to load',
                            type=str,
                            nargs='+')

    def handle(self, *args, **options):
        total_urls = len(options['json_urls'])
        self.stdout.write(f'Updating database, total places: {total_urls}')

        for url_number, url in enumerate(options['json_urls'], start=1):
            response = requests.get(url)
            response.raise_for_status()
            place = response.json()
            load_place_to_db(place)
            self.stdout.write(f'{url_number}/{total_urls} places loaded')

        self.stdout.write('Database updated.')
