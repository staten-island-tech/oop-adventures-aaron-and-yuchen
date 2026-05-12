import requests

def dealerdraw(amount):
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
        elif Dcardvalue == 21 and Dfirst_draw == True:
            print("Woah wth")

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
    def __init__(self, name):
        self.name = name
        self.money_given = 0
    
    def collected_bets(self, money):
        self.money_given += money
    
    def payout(self):
        print(f"{self.name} has paid out {self.money_given} dollars to the winner")
        self.money_given = 0

bob = Dealer("bob")
bob.Ddraw()