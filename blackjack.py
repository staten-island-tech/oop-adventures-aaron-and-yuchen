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
            playerwin = "Lose"
            print("yo why do you AND the dealer sucks")
            self.anger -= 1
            self.angergain = "L"
        elif Dcardvalue > cardvalue and dealerbust == True:
            playerwin = "Win"
            self.anger += 2
            self.angergain = "G"

    def __init__(self, name):
        self.name = name
        self.anger = 0
        self.angergain = "N/A"

    def angercheck(self):
        if self.anger >= 4 and self.anger < 8 and self.angergain == "G" and playerwin != "Lose": 
            print(f"{self.name}: You were just lucky that round...")      
        if self.anger >= 8 and self.anger < 12 and self.angergain == "G" and playerwin != "Lose": 
            print(f"{self.name}: Seriously, stop that.") 
        if self.anger >= 12 and self.anger < 16 and self.angergain == "G" and playerwin != "Lose": 
            print(f"{self.name}: You don't wanna see me angry... 'cus when I get angry... I see red...")
            print(f"{self.name}: 'cus when I get angry... I see red...")
            print(f"{self.name}: and when I see red... you better run...")
        if self.anger >= 16 and self.anger < 20 and self.angergain == "G" and playerwin != "Lose": 
            print(f"{self.name}: I HATE YOU, I'LL MAKE SURE YOU DIE HORRIBLY")
        if self.anger >= 20 and self.angergain == "G" and playerwin != "Lose": 
            print(f"{self.name}: GET OUT RIGHT NOW, AND NEVER COME BACK!!!")
            print(f"You were thrown out with ${money}")     
            exit()
        if self.anger <= -4 and self.anger > -8 and self.angergain == "L" and playerwin != "Win":
            print(f"{self.name}: You're not very good at this.")
        if self.anger <= -8 and self.anger > -12 and self.angergain == "L" and playerwin != "Win":
            print(f"{self.name}: You suck at this.")
        if self.anger <= -12 and self.anger > -16 and self.angergain == "L" and playerwin != "Win":
            print(f"{self.name}: I think, uh, you should think more carefully about your plays...")
        if self.anger <= -16 and self.anger > -20 and self.angergain == "L" and playerwin != "Win":
            print(f"{self.name}: You've lost... quite a lot now...")
        if self.anger <= -20 and self.angergain == "L" and playerwin != "Win":
            print(f"{self.name}: Ok look, I think you should just leave now, your obviously not gonna win anything.")
            print(f"You were kindly pointed to the exit with ${money}")     
            exit()

class Player:
    global bets
    bets = False
    def __init__(self, name, balance):
        self.name = name
        self.drunk = 0
        self.drunkup = False
        self.dnum = 0
        self.ds1 = 0
        self.ds2 = 0
        self.ds3 = 0
        self.ds4 = 0
        self.ds5 = 0
        self.__balance = balance
        self.stay = "yes"
        global money
        money = self.__balance

    def pregamemessage(self):
        print("READ FIRST: Your goal is to not go over 21 but still be higher than the opponent. Numbered cards have the same value as it shows. J, Q, K, and 0 are 10. A is 1 or 11 (Depending on how much you have).")
        print(f"You start with ${self.__balance}")

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
            self.__balance += y + y/2
        print(f"You now have {self.__balance}")

    def play(self):
        draw(2)

    def moneycheck(self):
        if self.__balance == 0:
            print("You suck now get out")
            exit()
        money = self.__balance
        self.stay = input("Keep playing? ").lower()
        while self.stay != "yes" or self.stay != "no":
            if self.stay == "no":
                    print(f"You left with ${self.__balance}  and {self.dnum} drinks taken.")
                    exit()
            elif self.stay == "yes":
                return
            print("Enter a valid response")
            self.stay = input("Keep playing? ").lower()

    def waiter(self):
        drink = input("A waiter comes by with a tray of drink, do you want one? ").lower()
        while drink != "yes" or drink != "no":
            if drink == "yes":
                print("You take one.")
                self.drunk += 2
                self.dnum += 1
                self.drunkup = True
                return
            elif drink == "no":
                print("He walks away.")
                if self.drunk != 0:
                    self.drunk -= 1
                self.drunkup = False
                return
            else:
                print("What?")
                if self.drunk != 0:
                    self.drunk -= 1
                self.drunkup = False
                return
            
    def drunkcheck(self):
        if self.drunk >= 4 and self.drunk < 8 and self.drunkup == True and self.ds1 == 0:
            print("You feel a little more confident.")
            self.ds1 = 1
        if self.drunk >= 8 and self.drunk < 12 and self.drunkup == True and self.ds2 == 0:
            print("You're vision is a little unclear.")
            self.ds2 = 1
        if self.drunk >= 12 and self.drunk < 16 and self.drunkup == True and self.ds3 == 0:
            print("You almost dozed off.")
            self.ds3 = 1
        if self.drunk >= 16 and self.drunk <= 20 and self.drunkup == True and self.ds4 == 0:
            print("You can't even see your cards anymore.")
            self.ds4 = 1
        if self.drunk > 20 and self.drunkup == True and self.ds5 == 0:
            print(f"You were escorted out after you started a fight with the dealer, you had ${self.__balance} and {self.dnum} drinks drunk.")
            self.ds5 = 1
            exit()
            
        
            
pboy = Player(input("Enter your name: "), 100)
Bob = Dealer("Bob")
loop = True
pboy.pregamemessage()
while loop == True:
        pboy.setbet()
        pboy.play()
        Bob.Ddraw()
        pboy.checkbet()
        Bob.angercheck()
        pboy.waiter()
        pboy.drunkcheck()
        pboy.moneycheck()