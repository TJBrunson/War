from card_pile import Card_Pile
from deck import Deck
class Player:
    
    #Currently create with list as hand. Empty list is default
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    #Returns if hand has any cards in it
    def has_cards(self):
        return len(self.hand) > 0
    
    def play_card(self, card_pile):
         card_pile.add_card(self.hand.pop(0), self) # want to pop top card off stack
    
    '''
    1. If there is a tie, players will each add 3 cards to the tie pile.
    2. If a player doesnt have 3 cards, add len(hand)-1 cards to leave one card left over to play with
    3. In the event there is a double tie and a player has 0 cards left (after 2) return False so
    the game board knows the player is unable to play and that they are out of the game
    '''
    def play_tie_breaker_cards(self, card_pile):
        #if hand is empty, return false
        if not self.has_cards: return False
        
        #do if players hand is greater than three
        if len(self.hand) > 3:
            card_pile.add_to_tie_pile(self.hand[0:3])
            self.hand = self.hand[3:]
            return True
        
        #add all but last card to tie pile and set hand to last card only
        num_cards = len(self.hand)
        if num_cards > 1:
            card_pile.add_to_tie_pile(self.hand[:-1])
            self.hand = self.hand[-1:]
        return True
        
    
    #Adds list of cards to hand
    def add_all_cards(self, cards):
        self.hand.extend(cards)