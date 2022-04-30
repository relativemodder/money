from models import Coin
from models import Weight
from random import randint

def generate_coins():
    coins = []
    random_fake_position = randint(0, 99)
    print(random_fake_position)
    for i in range(100):
        if i == random_fake_position:
            fake_coin = Coin(Weight.LIGHT, 1)
            coins.append(fake_coin)
        normal_coin = Coin(Weight.NORMAL, 1)
        coins.append(normal_coin)
    return coins