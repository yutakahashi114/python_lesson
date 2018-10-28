from sympy import *
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def get_card(self):
        card = self.rank + ' of ' + self.suit
        return card

def create_cart(suit, deck):
    for number in range(1, 14):
        if number == 1:
            rank = 'ace'
        elif number == 11:
            rank = 'jack'
        elif number == 12:
            rank = 'queen'
        elif number == 13:
            rank = 'king'
        else:
            rank = str(number)
        deck.append(Card(suit, rank))

if __name__ == '__main__':
    deck = []
    suit = 'spades'
    create_cart(suit, deck)
    suit = 'clubs'
    create_cart(suit, deck)
    suit = 'hearts'
    create_cart(suit, deck)
    suit = 'diamonds'
    create_cart(suit, deck)
    for card in deck:
        print(card.get_card())
    random.shuffle(deck)
    print('----------shuffled----------')
    for card in deck:
        print(card.get_card())
