from apis.rate_exchangeapi import RateExchangeAPI

COINS = ['USD', 'EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'LTL', 'LVL', 'PLN', 'RON', 'SEK', 'CHF', 'NOK', 'HRK', 'RUB',
         'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB',
         'ZAR', 'ISK']


class CoinManager():
    def __init__(self, coin):
        self.coin = self._get_coin_or_default(coin)
        self.rate = 0

    def create(self):
        self.rate = RateExchangeAPI().get_rate_from_usd_to(self.coin)

    def convert(self, value):
        return self.rate * value

    def _get_coin_or_default(self, coin):
        if coin in COINS:
            return coin
        else:
            return self._dollar_coin

    @property
    def _dollar_coin(self):
        return COINS[0]
