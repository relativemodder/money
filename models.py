class Coin:
    def __init__(self, weight: int, price: int):
        self.weight = weight
        self.price = price
    weight: int
    price: int
class Weigher:
    def __init__(self):
        pass
    def compare_coins(self, coin1: Coin, coin2: Coin) -> Coin:
        '''
        Returns a Coin with lighter weight
        '''
        if coin1.weight < coin2.weight:
            return coin1
        return coin2
    def compare_coin_lists(self, coins1: list[Coin], coins2: list[Coin]) -> list[Coin]:
        '''
        Returns list of Coin with lighter weight
        '''
        weight_first = 0
        weight_second = 0
        for coin in coins1:
            try:
                weight_first += coin.weight
            except:
                print("NoneType found!")
        for coin in coins2:
            try:
                weight_second += coin.weight
            except:
                print("NoneType found!")
        if weight_first < weight_second:
            return coins1
        return coins2
class Weight:
    NORMAL: int = 2
    LIGHT: int = 1