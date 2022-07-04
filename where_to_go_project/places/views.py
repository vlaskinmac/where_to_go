from django.shortcuts import render

# Create your views here.

from . models import Place


def index(request):
    for properties in Place.objects.all():
        # place = properties.details_place

        # "title": "Крыши24.рф",
        # "placeId": "roofs24",
        # "detailsUrl": "{{ properties }}"

        data = {"detailsUrl": properties.details_place,
                "title": properties.title_place,
                "placeId": properties.placeId,
                }
    return render(request, 'places/index.html', context=data)