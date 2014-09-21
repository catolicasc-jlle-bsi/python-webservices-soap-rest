import requests


class GoogleAPI:
    URL = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s,%s&sensor=false'

    def __init__(self):
        pass

    def get_latitude_and_longitude(self, road_trip):
        url = GoogleAPI.URL % (road_trip.city, road_trip.state)
        response = requests.get(url)
        json = response.json()
        self._load_json(json)
        return self.latitude, self.longitude

    def _load_json(self, json):
        location = json['results'][0]['geometry']['location']
        self.latitude = location['lat']
        self.longitude = location['lng']