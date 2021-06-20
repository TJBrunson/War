import unittest
from game import Game
from deck import Deck
class TestMethods(unittest.TestCase):
    
    def test_deal_cards(self):
        #checks that each player when there are an even number has the right number of cards
        game = Game(['TestOne', 'TestTwo'])
        hands = [len(player.hand) for player in game.players]
        self.assertTrue(hands.count(26) == 2)
        
        #When there are an odd number of players, checks that hands are the right size and tie_pile has right number of cards
        game = Game(['test1', 'test2', 'test3'])
        hands = [len(player.hand) for player in game.players]
        self.assertTrue(hands.count(17) == 3 and len(game.card_pile.tie_pile) == 1)
    
    def test_deck_building(self):
        
        deck = Deck()
        self.assertTrue(len(deck.cards) == 52)
        self.assertTrue(len([card for card in deck.cards if card.suit.value == 'Spades']) == (52/4))
        self.assertTrue(len([card for card in deck.cards if card.suit.value == 'Hearts']) == (52/4))
        self.assertTrue(
            len([card for card in deck.cards if card.suit.value == 'Diamonds']) == (52/4))
        self.assertTrue(
            len([card for card in deck.cards if card.suit.value == 'Clubs']) == (52/4))
    
    def test_remove_players(self):
        game = Game(['player1', 'player2', 'player3'])
        game.remove_players(game.players[0])
        self.assertIsNone(next((player for player in game.players if player.name == 'player1'),None))