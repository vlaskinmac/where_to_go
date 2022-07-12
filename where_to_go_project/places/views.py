from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from django.template.response import TemplateResponse
from django.urls import reverse

from . models import Place


def start_page(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(get_place, args=[place.id])
                }
            }
        )
    geo = {
        "type": "FeatureCollection",
        "features": features,
    }
    context = {"places": geo}
    return TemplateResponse(request, "places/index.html", context)


def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_details = {
        "title": place.title,
        "imgs": [img.image.url for img in place.imges.order_by('image_number')],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng,
        },
    }

    return JsonResponse(
        place_details,
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False,
        }
    )
