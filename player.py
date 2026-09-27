"""Lab 2
Christian Doss
Represents a player who has a wallet of coins and a object to toss
9/27/2026"""


from coin import Coin

class Player:
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def get_name(self):
        return self.__name

    def get_wallet(self):
        return self.__wallet

    def update_wallet(self, amount):
        self.__wallet += amount

    def toss_coin(self):
        self.__coin.toss()

    def get_coin_side(self):
        return self.__coin.get_sideup()

