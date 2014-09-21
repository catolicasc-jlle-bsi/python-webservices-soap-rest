import requests
import json as json_library
from utils.helper import is_number


class GasFeedAPI():
    URL = 'http://devapi.mygasfeed.com/stations/radius/%s/%s/%s/pre/price/rfej9napna.json?callback=?'

    def __init__(self):
        self.miles_radius = 2

    def get_gasoline_price(self, road_trip):
        self.road_trip = road_trip
        self._get()
        self._try()

        return self.gasoline_price

    def _get(self):
        url = GasFeedAPI.URL % (self.road_trip.latitude, self.road_trip.longitude, self.miles_radius)
        raw_response = requests.get(url)
        self.json = self._load_json(raw_response)

    def _load_json(self, raw_response):
        response = raw_response.text[2:-1]
        return json_library.loads(response)

    def _try(self):
        stations = self.json['stations']
        for station in stations:
            raw_gasoline = station['reg_price']
            if is_number(raw_gasoline):
                break
            else:
                raw_gasoline = None

        self._set_gasoline_or_try_with_more_miles_radius(raw_gasoline)

    def _set_gasoline_or_try_with_more_miles_radius(self, raw_gasoline):
        if raw_gasoline:
            self.gasoline_price = float(raw_gasoline)
        else:
            self.miles_radius += 1
            self._get()