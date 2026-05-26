import requests

def draw(amount):
        global first_deck
        first_deck = True
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
        if int(cards_drawn["remaining"]) <= 0:
            print("You are out of cards...")
            response = requests.get("https://deckofcardsapi.com/api/deck/1nze49wxn3h1/shuffle/")
            print("The deck has been shuffled!")
        elif int(cards_drawn["remaining"]) <= 0 and first_deck == True:
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
            print(f"{cards[y]['code'][0]} of {cards[y]['code'][1]}")
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
                print(f"Total: {cardvalue}")
            else:
                print(f"Total: {cardvalue}")
        while cardvalue < 21:
            hit_status = input("Hit or Stand ").lower()
            if hit_status == "hit":
                hit("yes", 1)
            elif hit_status == "stand":
                break
            else: 
                print("Enter a valid choice")
        if cardvalue == 21 and first_draw == False:
            print("Yay 21!")
        elif cardvalue > 21:
            print("Haha you busted")
            playerbust = True
        elif cardvalue == 21 and first_draw == True:
            print("Wow you got blackjack!!!")

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
            print(f"{cards[y]['code'][0]} of {cards[y]['code'][1]}")
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
                print(f"Total: {cardvalue}")
            else:
                print(f"Total: {cardvalue}")
    elif amount != 1:
        print("You are only allowed to draw one card per hit.")

def dealerdraw(amount):
        first_deck = False
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
        global Dresponse
        Dresponse = requests.get(f"https://deckofcardsapi.com/api/deck/1nze49wxn3h1/draw/?count={amount}")
        if Dresponse.status_code != 200:
            print("Error fetching data!")
            return None
        global Dcards_drawn
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
            print(f"{Dcards[y]['code'][0]} of {Dcards[y]['code'][1]}")
            Dcardvalue += int(Dcards[y]['value'])
            if Dcards[y]['value'] == 11:
                Daces.append(1)
                Dpresent = True
            if Dcardvalue > 21:
                if len(Daces) > 0 and Dpresent == True:
                    Dcardvalue -= 10
                    if len(Daces) == 0:
                        Dpresent = False
                print(f"Dealer's Total: {Dcardvalue}")
            else:
                print(f"Dealer's Total: {Dcardvalue}")
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
            print("Dealer got 21 son lock in")
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
            print(f"{Dcards[y]['code'][0]} of {Dcards[y]['code'][1]}")
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
                print(f"Dealer's Total: {Dcardvalue}")
            else:
                print(f"Dealer's Total: {Dcardvalue}")

class Dealer:
    def Ddraw(self):
        print("Dealer is drawing now...")
        dealerdraw(2)
        global playerwin
        playerwin = "Lose"
        if Dcardvalue > cardvalue and dealerbust == False:
            playerwin = "Lose"
            self.anger -= 2
            self.angergain = "L"
        elif Dcardvalue < cardvalue and playerbust == False and cardvalue != 21:
            playerwin = "Win"
            self.anger += 2
            self.angergain = "G"
        elif Dcardvalue == cardvalue and playerbust == False and dealerbust == False:
            playerwin = "Tie"
            self.anger -= 1
            self.angergain = "L"
        elif cardvalue == 21 and first_draw == True:
            playerwin = "Blackjack1"
            self.anger += 3
            self.angergain = "G"
        elif cardvalue == 21 and first_draw == False:
            playerwin = "Win"
            self.anger += 2
            self.angergain = "G"
        elif playerbust == True and dealerbust == True:
            print("yo why do you AND the dealer sucks")
            self.anger -= 1
            self.angergain = "L"
        elif Dcardvalue > cardvalue and dealerbust == True:
            playerwin = "Win"
            self.anger += 2
            self.angergain = "G"

        
    def __init__(self, name):
        self.name = name
        self.money_given = 0
        self.anger = 0
        self.angergain = "G"

    def angercheck(self):
        if self.anger == 0:
            ""
        if self.anger >= 4 and self.anger < 8 and self.angergain == "G": 
            print(f"{self.name}: You were just lucky that round...")      
        if self.anger >= 8 and self.anger < 12 and self.angergain == "G": 
            print(f"{self.name}: Seriously, stop that.") 
        if self.anger >= 12 and self.anger < 16 and self.angergain == "G": 
            print(f"{self.name}: You don't wanna see me angry... 'cus when I get angry... I see red...")
            print(f"{self.name}: 'cus when I get angry... I see red...")
            print(f"{self.name}: and when I see red... you better run...")
        if self.anger >= 16 and self.anger < 20 and self.angergain == "G": 
            print(f"{self.name}: I HATE YOU, I'LL MAKE SURE YOU DIE HORRIBLY")
        if self.anger >= 20 and self.angergain == "G": 
            print(f"{self.name}: GET OUT RIGHT NOW, AND NEVER COME BACK!!!")
            print(f"You were thrown out with ${money}")     
            exit()
        if self.anger <= -4 and self.anger > -8 and self.angergain == "L":
            print(f"{self.name}: You're not very good at this.")

class Player:
    global bets
    bets = False
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def setbet(self):
        integer = False
        global y
        while integer == False:
            try:
                bet = int(input("How much do you bet? "))
                integer = True
            except ValueError:
                print("Enter a valid integer buckaroo")
                
        y = bet
        while self.__balance - y < 0 or y <= 0:
            print(f"{self.name} must enter a valid 'bet' value.")
            integer = False
            while integer == False:
                try:
                    bet = int(input("How much do you bet? "))
                    integer = True
                except ValueError:
                    print("Enter a valid integer buckaroo")
            y = bet
        else:
            if bet > 0:
                print(f"{self.name} has made a bet of {y}")
                global bets
                bets = True

    def checkbet(self):
        if playerwin == "Lose":
            print("You lost")
            self.__balance -= y
        elif playerwin == "Win":
            print("You won")
            self.__balance += y
        elif playerwin == "Tie":
            print("You tied")
        elif playerwin == "Blackjack1":
            self.__balance += 1.5*y
        print(f"You now have {self.__balance}")

    def play(self):
        draw(1)

pboy = Player(input("Enter your name: "), 100)
Bob = Dealer("Bob")
money = 100
balance = pboy.__dict__
stay = "yes"
leave = False
print("So all the number value is their number, 0, J-K is 10 and A is 11 (1 if go over 21).")
print(f"You start with ${money}")
while money > 0 and leave == False:
    if stay == "yes":
        pboy.setbet()
        pboy.play()
        Bob.Ddraw()
        pboy.checkbet()
        Bob.angercheck()
        money = balance["_Player__balance"]
        if money == 0:
            print("You suck now get out")
            exit()
        stay = input("Keep playing? ").lower()
    elif stay == "no":
        print(f"You left with ${money}")
        leave = True
    else:
        print("Enter a valid response")
        stay = input("Keep playing? ").lower()



