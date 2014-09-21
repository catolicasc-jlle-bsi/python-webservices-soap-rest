from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
from model.coin_manager import CoinManager
from model.destiny import Destiny
from model.origin import Origin
from model.road_trip_manager import RoadTripManager
from model.road_trip_price import RoadTripPrice


dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://192.168.33.10:8008/",
    action = 'http://192.168.33.10:8008/',
    namespace = "http://example.com/sample.wsdl",
    prefix="ns0",
    trace = True,
    ns = True)

def taxi_service(city_origin, state_origin, city_destiny, state_destiny, coin):
    origin = Origin(city=city_origin, state=state_origin)
    destiny = Destiny(city=city_destiny, state=state_destiny)

    coin_manager = CoinManager(coin)
    coin_manager.create()

    road_trip_manager = RoadTripManager(origin, destiny, coin_manager)
    road_trip_manager.create()

    road_trip_price = RoadTripPrice(road_trip_manager)
    result_price = road_trip_price.total_price

    return {
        'origin': {
            'latitude': origin.latitude,
            'longitude': origin.longitude,
            'zip_code': origin.zip_code
        },
        'destiny': {
            'latitude': destiny.latitude,
            'longitude': destiny.longitude,
            'zip_code': destiny.zip_code
        },
        'km_distance': road_trip_manager.km_distance,
        'gasoline_price': road_trip_manager.gasoline_price,
        'total_price': result_price.price,
        'total_price_formatted': result_price.formatted
    }

# register the user function
dispatcher.register_function(
    'taxi_service',
    taxi_service,
    returns={
        'origin': {
            'latitude': float,
            'longitude': float,
            'zip_code': int
        },
        'destiny': {
            'latitude': float,
            'longitude': float,
            'zip_code': int
        },
        'km_distance': float,
        'gasoline_price': float,
        'total_price': float,
        'total_price_formatted': str
    },
    args={
        'city_origin': str,
        'state_origin': str,
        'city_destiny': str,
        'state_destiny': str,
        'coin': str
    }
    )


print "Starting server..."
httpd = HTTPServer(("192.168.33.10", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()