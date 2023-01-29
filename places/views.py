from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()

    feature_collection = {
      "type": "FeatureCollection",
      "features": []
    }

    for place in places:
        feature_collection['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lat, place.lng]
            },
            "properties": {
                "title": place.title,
                "placeId": f'place_{place.id}',
                "detailsUrl": reverse('place_details', args=[place.id])
            }
        })

    context = {'feature_collection': feature_collection}
    return render(request, 'index.html', context=context)


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    response = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
        }
    }
    return JsonResponse(response)
