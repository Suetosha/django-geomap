class PlaceGeoJSONSerializer:
    def __init__(self, queryset):
        self.queryset = queryset

    @staticmethod
    def feature(place):
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeId,
                "detailsUrl": f"/places/{place.placeId}/"
            }
        }

    def serialize(self):
        return {
            "type": "FeatureCollection",
            "features": [self.feature(place) for place in self.queryset]
        }


class PlaceDetailSerializer:

    def __init__(self, place):
        self.place = place

    def serialize(self):
        return {
            "title": self.place.title,
            "imgs": [img.image.url for img in self.place.images.all()],
            "description_short": self.place.description_short,
            "description_long": self.place.description_long,
            "coordinates": {
                "lat": self.place.lat,
                "lng": self.place.lng,
            },
        }
