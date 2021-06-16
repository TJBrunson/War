class Card_Pile:
    def __init__(self):
        super().__init__()
        self.cards = []
        self.players = []
        # if there is a high card tie, add tie breaker collection here for payout
        self.tie_pot = [] 
    
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
    def add_to_tie_pot(self, cards):
        self.tie_pot.extend(cards)