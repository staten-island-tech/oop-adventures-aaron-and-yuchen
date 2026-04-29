class Player:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def bet(self, bet):
        self.__balance = self.__balance - bet
    
    def show_balance(self):
        print(f"{self.name} currenly has {self.__balance} dollars")

pboy = Player("pboy", 100)
pboy.bet(10)
pboy.show_balance()