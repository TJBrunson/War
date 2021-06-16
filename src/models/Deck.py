class Deck:
    SUITS = ('H', 'S', 'D', 'C')
    CARD_RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A') # cards start at 2
    
    def __init__(self):
        super().__init__()
        self.cards = [[s,r] for s in Deck.SUITS for r in Deck.CARD_RANKS]
        for card in self.cards:
            print('{}-{}'.format(card[0], card[1]))

deck = Deck()
    