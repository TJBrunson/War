import random

class Deck:
    SUITS = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
    CARD_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace') # cards start at 2
    
    #Create list of cards based on suits and card ranks
    def __init__(self):
        self.cards = [[s,r] for s in Deck.SUITS for r in Deck.CARD_RANKS]
        
    #shuffle deck using random.shuffle
    def shuffle(self):
        random.shuffle(self.cards)