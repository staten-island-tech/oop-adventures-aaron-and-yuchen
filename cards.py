import requests

def draw(amount):
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
        print(f"There are {cards_drawn["remaining"]} cards remaining.")
        if amount > cards_drawn["remaining"] and cards_drawn["remaining"] != 0:
            print("Not enough cards, enter a valid value.")
            amount = 0
        elif cards_drawn['remaining'] == 0:
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
            print(cards[y])
            cardvalue += int(cards[y]['value'])
            if cards[y]['value'] == 11:
                aces.append(1)
                present = True
            if cardvalue > 21:
                if len(aces) > 0 and present == True:
                    cardvalue -= 10
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
        if amount > cards_drawn["remaining"] and cards_drawn["remaining"] != 0:
            print("Not enough cards, enter a valid value.")
            amount = 0
        elif cards_drawn['remaining'] == 0:
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
            print(cards[y])
            cardvalue += int(cards[y]['value'])
            if cards[y]['value'] == 11:
                aces.append(1)
                present = True
            if cardvalue > 21:
                if len(aces) > 0 and present == True:
                    cardvalue -= 10
                    present = False
                print(cardvalue)
            else:
                print(cardvalue)
        print(f"There are {cards_drawn["remaining"]} cards remaining.")
    elif amount != 1:
        print("You are only allowed to draw one card per hit.")

draw(2)

