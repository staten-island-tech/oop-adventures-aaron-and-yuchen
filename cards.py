import requests

def draw(amount):
        cards = {}
        response = requests.get(f"https://deckofcardsapi.com/api/deck/new/draw/?count={amount}")
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        cards_drawn = response.json()
        for x in range(amount):
                cards[x] = {
                    'code': cards_drawn['cards'][x]['code'],
                    'value': cards_drawn['cards'][x]['value'] 
                }
        print(cards)

draw(2)

