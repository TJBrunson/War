from Card_Pile import Card_Pile
class Player:
    
    #Currently create with list as hand. Empty list is default
    def __init__(self, name, hand=[]):
        super().__init__()
        self.name = name
        self.hand = hand
    
    #Returns if hand has any cards in it
    def has_cards(self):
        return bool(self.hand)
    
    def play_card(self, card_pile):
         card_pile.add_card(self.hand.pop(0), self) # want to pop top card off stack
    
    #Adds list of cards to hand
    def add_all_cards(self, cards):
        self.hand.extend(cards)