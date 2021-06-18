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
        to_remove = [] # make here because it is needed regardless of if there is a tie
        
        #if no winner returned, it means there is a tie
        if not winner:
            for player in self.players:
                can_play = player.play_tie_breaker_cards(card_pile)
                if not can_play: to_remove.append(player)
            self.remove_players(to_remove) #if tied, remove players who cannot compete in tie breaker
            self.play_round()
            return
        
        
        print("{} won this round".format(winner.name))
        self.card_pile.assign_winnings(winner)
        
        # After round remove players who run out of cards
        for player in self.players:
            if not player.has_cards: to_remove.append(player)
            
        # remove players that either could not enter tie break or 
        if len(to_remove) > 0:
            self.remove_players(to_remove)

        # if there is only one player left, return the player as the winner
        if(len(self.players) == 1): return self.players[0]

    #Remove all players in players_to_remove collection
    def remove_players(self, players_to_remove):
        for player in players_to_remove:
            self.players.remove(player)