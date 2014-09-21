import requests


class RedLineAPI():
    KEY = '4EUQSOB51gmjwAuh1l0kg60LUlsq3Ec7j7YbWzhXQDhndLEf7FzoLA9FVB6Yfj6z'
    URL_DISTANCE = 'http://zipcodedistanceapi.redline13.com/rest/%s/distance.json/%s/%s/km/'
    URL_ZIP_CODE = 'http://zipcodedistanceapi.redline13.com/rest/%s/city-zips.json/%s/%s'

    def __init__(self):
        pass

    def get_distance(self, origin, destiny):
        url = RedLineAPI.URL_DISTANCE % (RedLineAPI.KEY, origin.zip_code, destiny.zip_code)
        response = requests.get(url)
        json = response.json()
        self._load_json_distance(json)
        return self.distance

    def _load_json_distance(self, json):
        self.distance = json['distance']

    def get_zip_code(self, road_trip):
        url = RedLineAPI.URL_ZIP_CODE % (RedLineAPI.KEY, road_trip.city, road_trip.state)
        response = requests.get(url)
        json = response.json()
        self._load_json_zip_code(json)
        return self.zip_code

    def _load_json_zip_code(self, json):
        zip_codes = json['zip_codes']
        self.zip_code = self._get_first_zip_code(zip_codes)

    def _get_first_zip_code(self, zip_codes):
        return int(zip_codes[0])