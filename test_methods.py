import unittest
from game import Game
from deck import Deck, Card, Suits
from player import Player
from card_pile import Card_Pile
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
        #Test removing single player
        game = Game(['player1', 'player2', 'player3'])
        game.remove_players([game.players[0]])
        self.assertIsNone(next((player for player in game.players if player.name == 'player1'),None))
        
        #Test removing more than one player at a time
        game.players.append(Player("test4",[]))
        game.remove_players([game.players[0], game.players[1]])
        self.assertTrue(len(game.players) == 1)
        
    def test_play_round(self):
        #Test winner returned if only one player left after round
        game = Game(['player1', 'player2'])
        game.players[0].hand = [Card(Suits.Spades, '2')]
        game.players[1].hand = [Card(Suits.Spades, '3')]
        winner = game.play_round()
        self.assertTrue(winner.name == 'player2')
        
        #test tie when players have more than 4 cards
        game = Game(['player1', 'player2'])
        game.players[0].hand = [
            Card(Suits.Spades, '2'), Card(Suits.Spades, '3'), Card(Suits.Spades, '4'), Card(Suits.Spades, '8'), Card(Suits.Spades, '7'), Card(Suits.Spades, '5')]
        game.players[1].hand = [
            Card(Suits.Spades, '2'), Card(Suits.Spades, '3'), Card(Suits.Spades, '8'), Card(Suits.Spades, '10'), Card(Suits.Spades, '6'), Card(Suits.Spades, '7')]
        winner = game.play_round()
        self.assertTrue(len(game.players[0].hand) == 11)
        self.assertTrue(len(game.players[1].hand) == 1)
        self.assertTrue(len(game.players) == 2)
        

        #test tie when player2 doesnt have more than 4 cards but wins
        game = Game(['player1', 'player2'])
        game.players[0].hand = [
            Card(Suits.Spades, '2'), Card(Suits.Spades, '3'), Card(Suits.Spades, '4'), Card(Suits.Spades, '8'), Card(Suits.Spades, '7'), Card(Suits.Spades, '5')]
        game.players[1].hand = [
            Card(Suits.Spades, '2'), Card(Suits.Spades, '3'), Card(Suits.Spades, '8'), Card(Suits.Spades, '10')]
        winner = game.play_round()
        self.assertTrue(len(game.players[0].hand) == 1)
        self.assertTrue(len(game.players[1].hand) == 9)
        self.assertTrue(len(game.players) == 2)
        
        #test tie when player2 doesnt have more than 4 cards but loses
        game = Game(['player1', 'player2'])
        game.players[0].hand = [
            Card(Suits.Spades, '2'), Card(Suits.Spades, '3'), Card(Suits.Spades, '4'), Card(Suits.Spades, '8'), Card(Suits.Spades, '7'), Card(Suits.Spades, '5')]
        game.players[1].hand = [
            Card(Suits.Spades, '2'), Card(Suits.Spades, '3'), Card(Suits.Spades, '8'), Card(Suits.Spades, '7')]
        winner = game.play_round()
        self.assertTrue(len(game.players[0].hand) == 10)
        self.assertTrue(len(game.players) == 1)

    #Tests winning and getting winnings
    def test_card_pile_winner(self):
        player1 = Player('p1', [Card(Suits.Clubs, '2'), Card(
            Suits.Clubs, '3'), Card(Suits.Clubs, '4')])
        player2 = Player('p2', [Card(Suits.Clubs, '5'), Card(
            Suits.Clubs, '6'), Card(Suits.Clubs, '7')])
        
        card_pile = Card_Pile()
        
        #Testing length of piles after playing cards
        player1.play_card(card_pile)
        player2.play_card(card_pile)
        self.assertTrue(len(card_pile.cards) == 2)
        self.assertTrue (len(card_pile.players) == 2)
        
        #Testing that the winner is correct
        winner = card_pile.winner ()
        self.assertTrue(winner == player2)
        #Testing that the winner has the right amount of cards after collecting winnings
        card_pile.assign_winnings(winner)
        self.assertTrue(len(player2.hand) == 4)
        
