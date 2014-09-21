import requests


class RateExchangeAPI():
    URL = 'http://rate-exchange.appspot.com/currency?from=USD&to=%s'

    def __init__(self):
        pass

    def get_rate_from_usd_to(self, coin):
        url = RateExchangeAPI.URL % coin
        response = requests.get(url)
        json = response.json()
        self._load_json(json)
        return self.rate

    def _load_json(self, json):
        self.rate = json['rate']

