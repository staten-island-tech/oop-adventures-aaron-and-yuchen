class Player:
    global bets
    bets = False
    money_lost = 0
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        global x
        x = balance
    
    def bet(self, bet):
        global y
        y = bet
        if self.__balance - y < 0:
            print(f"{self.name} does not have enough money to make this bet")
        else:
            if bet >= 0:
                self.__balance = self.__balance - y
                print(f"{self.name} has made a bet of {y}")
                global bets
                bets = True
            else: 
                print("Please make a valid bet")
    
    def double(self):
        if self.__balance - y or bets == False < 0:
            print(f"{self.name} does not have enough money to double their bet")
        else: 
            self.__balance = self.__balance - y
            print(f"{self.name} has successfully doubled their bet")
            bets == False

    def show_balance(self):
        print(f"{self.name} currently has {self.__balance} dollars")

    def money_gained(self):
        money = self.__balance - x
        if self.__balance > x:
            print(f"{self.name} has gained {money} dollars")
        else: 
            print("You have not made any money.")

pboy = Player("pboy", 100)
pboy.bet(51)
pboy.double()
pboy.show_balance()
pboy.money_gained()