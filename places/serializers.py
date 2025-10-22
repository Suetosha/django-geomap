
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
                "detailsUrl": ''
            }
        }

    def serialize(self):
        return {
            "type": "FeatureCollection",
            "features": [self.feature(place) for place in self.queryset]
        }
