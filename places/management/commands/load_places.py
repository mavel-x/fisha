from io import BytesIO
from pathlib import Path
from urllib.parse import urlsplit

import requests
from django.core.management.base import BaseCommand
from django.core.files.images import ImageFile

from places.models import Place


def fetch_image(url: str):
    response = requests.get(url)
    response.raise_for_status()
    filename = Path(urlsplit(url).path).name
    return response.content, filename


def fetch_place(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


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
        image, filename = fetch_image(url)
        image_file = ImageFile(file=BytesIO(image), name=filename)
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
        self.stdout.write(f'Updating DB, total places: {total_urls}')

        for url_number, url in enumerate(options['json_urls'], start=1):
            place = fetch_place(url)
            load_place_to_db(place)
            self.stdout.write(f'{url_number}/{total_urls} places loaded')

        self.stdout.write('Database updated.')
