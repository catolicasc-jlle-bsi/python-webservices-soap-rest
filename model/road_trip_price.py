from model.resultprice import ResultPrice
from model.taxicar import TaxiCar


class RoadTripPrice():
    INITIAL_VALUE = 2.5

    def __init__(self, road_trip_manager):
        self.road_trip_manager = road_trip_manager
        self.price = 0

        self._calculate()

    def _calculate(self):
        self.price = RoadTripPrice.INITIAL_VALUE + (
        (self.road_trip_manager.km_distance / TaxiCar.KM_PER_LITER) * self.road_trip_manager.gasoline_price)

    @property
    def total_price(self):
        return ResultPrice(self.road_trip_manager.coin_manager.coin, self.price)
