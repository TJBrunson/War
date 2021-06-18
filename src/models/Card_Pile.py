from models.Deck import Deck
class Card_Pile:

    def __init__(self):
        super().__init__()
        self.cards = []
        self.players = []
        # if there is a high card tie, add tie breaker collection here for payout
        self.tie_pile = [] 
    
    '''
    want to append card and player to lists in order of card recieved
    can use the index of top card to judge which player should win the pot + bonus
    '''
    def add_card(self, card, player):
        self.cards.append(card)
        self.players.append(player)

    # prints who played what
    def show_card_pile(self):
        for player, card in zip(self.players, self.cards):
            print('{} played {}'.format( player.name, card))

    '''
    Players place 3 cards here when there is a tie for tie breaker round.
    When initial dealing is done, any remainder cards are added here to ensure all players
    start on an even playing field
    '''
    def add_to_tie_pile(self, cards):
        self.tie_pile.extend(cards)
        
    def show_pile(self):
        for player, card in zip(self.players, self.cards):
            print("{} played a {}".format(player.name,card))
            
    def winner(self):
        # Get list of value of each card (not suit) and then convert to list of ranks based on index
        vals = [Deck.CARD_RANKS.index(val) for val in [card[1]  for card in self.cards]]
        if vals.count(max(vals)) == 1:
            return self.players[vals.index(max(vals))]
    
    def move_cards_to_tie_pile(self):
        self.add_to_tie_pile(self.cards)
        self.cards = []
        self.players = []
    
    def assign_winnings(self, winner):
        winnings = self.cards + self.tie_pile
        winner.add_all_cards(winnings)
        self.cards = []
        self.tie_pile = []
        self.players = []
