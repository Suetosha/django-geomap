from django.http import JsonResponse
from django.shortcuts import render
import json

from places.models import Place
from places.serializers import PlaceGeoJSONSerializer, PlaceDetailSerializer


def index(request):
    try:
        if request.method == "GET":
            places = Place.objects.all()
            places_geojson = PlaceGeoJSONSerializer(places).serialize()
            return render(request, "index.html", {"places_geojson": json.dumps(places_geojson, ensure_ascii=False)})
        else:
            raise Exception("Method not supported")

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def places(request, place_id):
    try:
        if request.method == "GET":
            place = Place.objects.get(placeId=place_id)
            place_json = PlaceDetailSerializer(place).serialize()

            return JsonResponse(place_json)
        else:
            raise Exception("Method not supported")

    except Place.DoesNotExist:
        return JsonResponse({"error": "Place not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
