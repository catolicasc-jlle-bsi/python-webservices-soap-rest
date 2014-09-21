from apis import GoogleAPI, RedLineAPI, GasFeedAPI


class RoadTripManager():
    def __init__(self, origin, destiny, coin_manager):
        self.origin = origin
        self.destiny = destiny
        self.gasoline_price = 0
        self.km_distance = 0
        self.coin_manager = coin_manager

    def create(self):
        self._set_latitude_and_longitude(self.origin)
        self._set_latitude_and_longitude(self.destiny)

        self._set_zip_code(self.origin)
        self._set_zip_code(self.destiny)

        self._set_distance()

        self._set_gas_price(self.origin)

    def _set_latitude_and_longitude(self, road_trip):
        road_trip.latitude, road_trip.longitude = GoogleAPI().get_latitude_and_longitude(road_trip)

    def _set_zip_code(self, road_trip):
        road_trip.zip_code = RedLineAPI().get_zip_code(road_trip)

    def _set_distance(self):
        self.km_distance = RedLineAPI().get_distance(self.origin, self.destiny)

    def _set_gas_price(self, road_trip):
        gasoline_price = GasFeedAPI().get_gasoline_price(road_trip)
        self.gasoline_price = self.coin_manager.convert(gasoline_price)