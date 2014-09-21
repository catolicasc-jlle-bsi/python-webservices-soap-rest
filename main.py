from model import Origin, Destiny, RoadTripManager, RoadTripPrice
from model.coin_manager import CoinManager
import sys


if __name__ == '__main__':
    # python main.py new%20york ny san%20francisco ca BRL

    origin = Origin(city=sys.argv[1], state=sys.argv[2])
    destiny = Destiny(city=sys.argv[3], state=sys.argv[4])
    coin = sys.argv[5]

    coin_manager = CoinManager(coin)
    coin_manager.create()

    road_trip_manager = RoadTripManager(origin, destiny, coin_manager)
    road_trip_manager.create()

    road_trip_price = RoadTripPrice(road_trip_manager)
    print road_trip_price.total_price
