from models.player import Player
from models.deck import Deck
from models.card_pile import Card_Pile

class Game:
    
    def __init__(self, player_names):
        self.players = [Player(player_name, []) for player_name in player_names]
        self.card_pile = Card_Pile()
        self.deck = Deck()
        self.deck.shuffle() # shuffle cards before dealing
        self.deal_cards()
        for player in self.players:
            print(player.name, player.hand)
    
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
            print("There was a tie!")
            self.card_pile.move_cards_to_tie_pile()
            for player in self.players:
                can_play = player.play_tie_breaker_cards(self.card_pile)
                if not can_play: to_remove.append(player)
            self.remove_players(to_remove) #if tied, remove players who cannot compete in tie breaker
            self.play_round()
            return
        
        print("{} won this round".format(winner.name))
        self.card_pile.assign_winnings(winner)
        
        # After round remove players who run out of cards
        for player in self.players:
            print("{} has {} cards left".format(player.name, len(player.hand)))
            if not len(player.hand) > 0: to_remove.append(player)
            
        # remove players that either could not enter tie break or 
        if len(to_remove) > 0:
            self.remove_players(to_remove)

        # if there is only one player left, return the player as the winner
        if(len(self.players) == 1): return self.players[0]

    #Remove all players in players_to_remove collection
    def remove_players(self, players_to_remove):
        for player in players_to_remove:
            print("{} ran out of cards and is out of the game!".format(player.name))
            self.players.remove(player)