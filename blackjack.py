import requests

def draw(amount):
        global playerbust
        playerbust = False
        global first_draw
        first_draw = True
        global present
        present = False
        cards = {}
        global aces
        aces = []
        global cardvalue
        cardvalue = 0
        response = requests.get(f"https://deckofcardsapi.com/api/deck/1nze49wxn3h1/draw/?count={amount}")
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        cards_drawn = response.json()
        if cards_drawn['remaining'] != 1:
            print(f"There are {cards_drawn["remaining"]} cards remaining.")
        else: 
            print("There are 0 cards remaining")
        if cards_drawn['remaining'] == 0:
            print("You are out of cards...")
            response = requests.get("https://deckofcardsapi.com/api/deck/1nze49wxn3h1/shuffle/")
            print("The deck has been shuffled!")
            return None
        if int(cards_drawn["remaining"]) <= 0:
            print("You are out of cards...")
            response = requests.get("https://deckofcardsapi.com/api/deck/1nze49wxn3h1/shuffle/")
            print("The deck has been shuffled!")
        for x in range(amount):
            if cards_drawn['cards'][x]['value'] == 'QUEEN' or cards_drawn['cards'][x]['value'] == 'KING' or cards_drawn['cards'][x]['value'] == 'JACK':
                cards[x] = {
                    'code': cards_drawn['cards'][x]['code'],
                    'value': 10,
                    'suit': cards_drawn['cards'][x]['suit']
                }
            elif cards_drawn['cards'][x]['value'] == 'ACE':
                cards[x] = {
                    'code': cards_drawn['cards'][x]['code'],
                    'value': 11,
                    'suit': cards_drawn['cards'][x]['suit']
                }
            else:
                cards[x] = {
                    'code': cards_drawn['cards'][x]['code'],
                    'value': cards_drawn['cards'][x]['value'],
                    'suit': cards_drawn['cards'][x]['suit']
                }
        for y in cards:
            print(cards[y]['code'])
            cardvalue += int(cards[y]['value'])
            if cards[y]['value'] == 11:
                aces.append(1)
                present = True
            if cardvalue > 21:
                if len(aces) > 0 and present == True:
                    cardvalue -= 10
                    if len(aces) == 0:
                        present = False
                print(cardvalue)
            else:
                print(cardvalue)
        while cardvalue < 21:
            hit_status = input("Hit or Stand ").lower()
            if hit_status == "hit":
                hit("yes", 1)
            elif hit_status == "stand":
                break
            else: 
                print("Enter a valid choice")
        if cardvalue == 21 and first_draw == False:
            print("Wow you won and got 21!!")
        elif cardvalue > 21:
            print("Haha you busted")
            playerbust = True
        elif cardvalue == 21 and first_draw == True:
            print("Wow you got blackjack!!! and pboy likes men")

def hit(yn, amount):
    global first_draw
    first_draw = False
    global present
    if yn == "yes" and amount == 1:
        if len(aces) > 1:
            present = True
        cards = {}
        global cardvalue
        response = requests.get(f"https://deckofcardsapi.com/api/deck/1nze49wxn3h1/draw/?count=1")
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        cards_drawn = response.json()
        if cards_drawn['remaining'] != 1:
            print(f"There are {cards_drawn["remaining"]} cards remaining.")
        else: 
            print("There are 0 cards remaining")
        if int(cards_drawn["remaining"]) <= 0:
            print("You are out of cards...")
            response = requests.get("https://deckofcardsapi.com/api/deck/1nze49wxn3h1/shuffle/")
            print("The deck has been shuffled!")
        for x in range(amount):
            if cards_drawn['cards'][x]['value'] == 'QUEEN' or cards_drawn['cards'][x]['value'] == 'KING' or cards_drawn['cards'][x]['value'] == 'JACK':
                cards[x] = {
                    'code': cards_drawn['cards'][x]['code'],
                    'value': 10,
                    'suit': cards_drawn['cards'][x]['suit']
                }
            elif cards_drawn['cards'][x]['value'] == 'ACE':
                cards[x] = {
                    'code': cards_drawn['cards'][x]['code'],
                    'value': 11,
                    'suit': cards_drawn['cards'][x]['suit']
                }
            else:
                cards[x] = {
                    'code': cards_drawn['cards'][x]['code'],
                    'value': cards_drawn['cards'][x]['value'],
                    'suit': cards_drawn['cards'][x]['suit']
                }
        for y in cards:
            print(cards[y]['code'])
            cardvalue += int(cards[y]['value'])
            if cards[y]['value'] == 11:
                aces.append(1)
                present = True
            if cardvalue > 21:
                if len(aces) > 0 and present == True:
                    cardvalue -= 10
                    aces.remove(1)
                    if len(aces) == 0:
                        present = False
                print(cardvalue)
            else:
                print(cardvalue)
    elif amount != 1:
        print("You are only allowed to draw one card per hit.")

def dealerdraw(amount):
        global DBJ
        DBJ = False
        global dealerbust
        dealerbust = False
        global Dfirst_draw
        Dfirst_draw = True
        global Dpresent
        Dpresent = False
        Dcards = {}
        global Daces
        Daces = []
        global Dcardvalue
        Dcardvalue = 0
        Dresponse = requests.get(f"https://deckofcardsapi.com/api/deck/1nze49wxn3h1/draw/?count={amount}")
        if Dresponse.status_code != 200:
            print("Error fetching data!")
            return None
        Dcards_drawn = Dresponse.json()
        if Dcards_drawn['remaining'] != 1:
            print(f"There are {Dcards_drawn["remaining"]} cards remaining.")
        else: 
            print("There are 0 cards remaining")
        if Dcards_drawn['remaining'] == 0:
            print("You are out of cards...")
            Dresponse = requests.get("https://deckofcardsapi.com/api/deck/1nze49wxn3h1/shuffle/")
            print("The deck has been shuffled!")
            return None
        if int(Dcards_drawn["remaining"]) <= 0:
            print("You are out of cards...")
            Dresponse = requests.get("https://deckofcardsapi.com/api/deck/1nze49wxn3h1/shuffle/")
            print("The deck has been shuffled!")
        for x in range(amount):
            if Dcards_drawn['cards'][x]['value'] == 'QUEEN' or Dcards_drawn['cards'][x]['value'] == 'KING' or Dcards_drawn['cards'][x]['value'] == 'JACK':
                Dcards[x] = {
                    'code': Dcards_drawn['cards'][x]['code'],
                    'value': 10,
                    'suit': Dcards_drawn['cards'][x]['suit']
                }
            elif Dcards_drawn['cards'][x]['value'] == 'ACE':
                Dcards[x] = {
                    'code': Dcards_drawn['cards'][x]['code'],
                    'value': 11,
                    'suit': Dcards_drawn['cards'][x]['suit']
                }
            else:
                Dcards[x] = {
                    'code': Dcards_drawn['cards'][x]['code'],
                    'value': Dcards_drawn['cards'][x]['value'],
                    'suit': Dcards_drawn['cards'][x]['suit']
                }
        for y in Dcards:
            print(Dcards[y]['code'])
            Dcardvalue += int(Dcards[y]['value'])
            if Dcards[y]['value'] == 11:
                Daces.append(1)
                Dpresent = True
            if Dcardvalue > 21:
                if len(Daces) > 0 and Dpresent == True:
                    Dcardvalue -= 10
                    if len(Daces) == 0:
                        Dpresent = False
                print(Dcardvalue)
            else:
                print(Dcardvalue)
        while Dcardvalue < 21:
            if Dcardvalue < 17:
                Dhit_status = "hit"
            elif Dcardvalue >=17: 
                Dhit_status = "stand"
            if Dhit_status == "hit":
                dealerhit("yes", 1)
            elif Dhit_status == "stand":
                break
        if Dcardvalue == 21 and Dfirst_draw == False:
            print("Dealer got blackjack son lock in")
        elif Dcardvalue > 21:
            print("Dealer busts")
            dealerbust = True
        elif Dcardvalue == 21 and Dfirst_draw == True:
            print("Woah wth")
            DBJ = True

def dealerhit(yn, amount):
    global Dfirst_draw
    Dfirst_draw = False
    global Dpresent
    if yn == "yes" and amount == 1:
        if len(Daces) > 1:
            Dpresent = True
        Dcards = {}
        global Dcardvalue
        Dresponse = requests.get(f"https://deckofcardsapi.com/api/deck/1nze49wxn3h1/draw/?count=1")
        if Dresponse.status_code != 200:
            print("Error fetching data!")
            return None
        Dcards_drawn = Dresponse.json()
        if Dcards_drawn['remaining'] != 1:
            print(f"There are {Dcards_drawn["remaining"]} cards remaining.")
        else: 
            print("There are 0 cards remaining")
        if int(Dcards_drawn["remaining"]) <= 0:
            print("You are out of cards...")
            Dresponse = requests.get("https://deckofcardsapi.com/api/deck/1nze49wxn3h1/shuffle/")
            print("The deck has been shuffled!")
        for x in range(amount):
            if Dcards_drawn['cards'][x]['value'] == 'QUEEN' or Dcards_drawn['cards'][x]['value'] == 'KING' or Dcards_drawn['cards'][x]['value'] == 'JACK':
                Dcards[x] = {
                    'code': Dcards_drawn['cards'][x]['code'],
                    'value': 10,
                    'suit': Dcards_drawn['cards'][x]['suit']
                }
            elif Dcards_drawn['cards'][x]['value'] == 'ACE':
                Dcards[x] = {
                    'code': Dcards_drawn['cards'][x]['code'],
                    'value': 11,
                    'suit': Dcards_drawn['cards'][x]['suit']
                }
            else:
                Dcards[x] = {
                    'code': Dcards_drawn['cards'][x]['code'],
                    'value': Dcards_drawn['cards'][x]['value'],
                    'suit': Dcards_drawn['cards'][x]['suit']
                }
        for y in Dcards:
            print(Dcards[y]['code'])
            Dcardvalue += int(Dcards[y]['value'])
            if Dcards[y]['value'] == 11:
                Daces.append(1)
                Dpresent = True
            if Dcardvalue > 21:
                if len(Daces) > 0 and Dpresent == True:
                    Dcardvalue -= 10
                    Daces.remove(1)
                    if len(Daces) == 0:
                        Dpresent = False
                print(Dcardvalue)
            else:
                print(Dcardvalue)

class Dealer:
    def Ddraw(self):
        dealerdraw(2)
        if Dcardvalue > cardvalue and dealerbust == False:
            playerwin == "Lose"
        elif Dcardvalue < cardvalue and playerbust == False or dealerbust == True:
            playerwin == "Win"
        elif Dcardvalue == cardvalue and playerbust == False and dealerbust == False:
            playerwin == "Tie"
        elif playerbust == True and dealerbust == True:
            print("yo why do you AND the dealer sucks")
        
    def __init__(self, name):
        self.name = name
        self.money_given = 0
    
    def collected_bets(self, money):
        self.money_given += money
    
    def payout(self):
        print(f"{self.name} has paid out {self.money_given} dollars to the winner")
        self.money_given = 0

class Player:
    global bets
    bets = False
    def __init__(self, name, balance):
        global playerwin
        playerwin = "Lose"
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
                print(f"{self.name} has made a bet of {y}")
                global bets
                bets = True
            else: 
                print("Please make a valid bet")
        if self.playerwin == False:
            print("You lost")
            self.__balance -= y
        elif self.playerwin == True:
            print("You won")
            self.__balance += y
        print(f"You now have {self.__balance}")
    
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

    def play(self):
        draw(2)

pboy = Player("pboy", 100)
bob = Dealer("bob")
pboy.play()
bob.Ddraw()