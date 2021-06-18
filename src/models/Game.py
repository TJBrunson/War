from Player import Player
from Deck import Deck
from Card_Pile import Card_Pile

class Game:
    
    def __init__(self, players):
        super().__init__()
        self.players = [Player(player, []) for player in players]
        self.card_pile = Card_Pile()
        self.deck = Deck()
        self.deck.shuffle() # shuffle cards before dealing
        self.deal_cards()
    
    '''
    While total number of cards is greater than number of players,
    add card to each player.
    return remainder cards to be added to tie_pile for first round winner
    '''
    def deal_cards(self):
        cards = self.deck.cards
        while len(cards) >= len(self.players):
            for player in self.players:
                card = cards[0] #get top card
                cards = cards[1:] # sub-list cards to remove top card
                player.hand.append(card) # add top card to layers hand
        self.card_pile.add_to_tie_pile(cards)
    
    def play_round(self):
        print("DRAW!!!")
        for player in self.players:
            if player.has_cards():
                player.play_card(self.card_pile)
        self.card_pile.show_pile()
        winner = self.card_pile.winner()
        if not winner:
            for player in self.players:
                card_pile.
        print("the winner is: {}".format(winner.name))
        self.card_pile.assign_winnings(winner)
        for player in self.players:
            print("{} has {} cards".format(player.name, len(player.hand)))

game = Game(["Tim", "Emily", "Steve"])
game.play_round()
