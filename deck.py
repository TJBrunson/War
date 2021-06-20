import random
from enum import Enum


class Suits(Enum):
    Spades = 'Spades'
    Hearts = 'Hearts'
    Diamonds = 'Diamonds'
    Clubs = 'Clubs'


class Deck:
    CARD_RANKS = (
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'Jack',
        'Queen',
        'King',
        'Ace')  # cards start at 2

    # Create list of cards based on suits and card ranks
    def __init__(self):
        self.cards = []
        for suit in Suits:
            for rank in Deck.CARD_RANKS:
                # self.cards.append([suit, rank])
                self.cards.append(Card(suit, rank))

    # shuffle deck using random.shuffle
    def shuffle(self):
        random.shuffle(self.cards)


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit.value)

    def rank_value(self):
        return Deck.CARD_RANKS.index(self.rank)
