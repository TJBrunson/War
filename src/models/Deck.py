import random
from enum import Enum
class Suits(Enum):
    Spades = 'Spades'
    Hearts = 'Hearts'
    Diamonds = 'Diamonds'
    Clubs = 'Clubs'

class Deck:
    CARD_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace') # cards start at 2
    
    #Create list of cards based on suits and card ranks
    def __init__(self):
        self.cards = []
        for suit in Suits:
            for rank in Deck.CARD_RANKS:
                self.cards.append([suit, rank])
        
    #shuffle deck using random.shuffle
    def shuffle(self):
        random.shuffle(self.cards)
        
deck = Deck()
print(deck.cards)