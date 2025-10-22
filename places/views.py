from django.shortcuts import render
import json

from places.models import Place
from places.serializers import PlaceGeoJSONSerializer


def index(request):
    places = Place.objects.all()
    db_geojson = PlaceGeoJSONSerializer(places).serialize()
    return render(request, "index.html", {"places_geojson": json.dumps(db_geojson, ensure_ascii=False)})
