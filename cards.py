import requests

def draw(amount):
        cards = {}
        cardvalue = 0
        response = requests.get(f"https://deckofcardsapi.com/api/deck/new/draw/?count={amount}")
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        cards_drawn = response.json()
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
                    'value_1': 1,
                    'value_11': 11,
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
        print(cardvalue)

draw(2)