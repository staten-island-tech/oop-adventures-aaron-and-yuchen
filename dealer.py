class Dealer:
    def __init__(self, name):
        self.name = name
        self.money_given = 0
    
    def collected_bets(self, money):
        self.money_given += money
    
    def payout(self):
        print(f"{self.name} has paid out {self.money_given} dollars to the winner")
        self.money_given = 0

bob = Dealer("bob")
bob.collected_bets(100)
bob.payout()
bob.collected_bets(10)
bob.payout()