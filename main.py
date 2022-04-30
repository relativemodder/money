from generators import generate_coins
from models import Coin, Weigher
from utils import chunk_list


def main():
    coins = generate_coins()
    weigher = Weigher()
    current_coin_list: list[Coin] = []
    current_coin_list = list(coins)
    fake = Coin(0, 0)
    while True:
        halfs = chunk_list(current_coin_list, current_coin_list.__len__()//2)
        first_half = halfs[0]
        second_half = halfs[1]
        
        lighter_list = weigher.compare_coin_lists(first_half, second_half)
        current_coin_list = list(lighter_list)
        if(current_coin_list.__len__() == 1):
            fake = current_coin_list[0]
            break
    print("Ready!")
    print(fake)
    
    
if __name__ == "__main__":
    main()