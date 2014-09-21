

class ResultPrice():
    def __init__(self, coin, price):
        self.coin = coin
        self.price = price

    def value(self):
        return self.price

    @property
    def formatted(self):
        return '%s %s' % (self.coin, self.price)

    def __str__(self):
        return self.formatted