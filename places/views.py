from django.shortcuts import render

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
                "placeId": place.slug,
                "detailsUrl": f"https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/{place.slug}.json"
            }
        })

    context = {'feature_collection': feature_collection}
    return render(request, 'index.html', context=context)
