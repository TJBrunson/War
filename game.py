from player import Player
from deck import Deck
from card_pile import Card_Pile


class Game:

    def __init__(self, player_names):
        self.players = [Player(player_name, [])
                        for player_name in player_names]
        self.card_pile = Card_Pile()
        self.deck = Deck()
        self.deck.shuffle()  # shuffle cards before dealing
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
                card = cards[0]  # get top card
                cards = cards[1:]  # sub-list cards to remove top card
                player.hand.append(card)  # add top card to layers hand
        self.card_pile.add_to_tie_pile(cards)

    def play_round(self):
        for player in self.players:
            if player.has_cards():
                player.play_card(self.card_pile)
        self.card_pile.show_pile()
        winner = self.card_pile.winner()
        to_remove = []  # make here because it is needed regardless of if there is a tie

        # if no winner returned, it means there is a tie
        if not winner:
            print("There was a tie!")
            self.card_pile.move_cards_to_tie_pile()
            for player in self.players:
                can_play = player.play_tie_breaker_cards(self.card_pile)
                if not can_play:
                    to_remove.append(player)
            # if tied, remove players who cannot compete in tie breaker
            self.remove_players(to_remove)
            self.play_round()
            return None

        print("{} won this round".format(winner.name))
        self.card_pile.assign_winnings(winner)

        # After round remove players who run out of cards
        for player in self.players:
            print("{} has {} cards left".format(player.name, len(player.hand)))
            if len(player.hand) == 0:
                to_remove.append(player)

        # remove players that either could not enter tie break or
        self.remove_players(to_remove)

        # if there is only one player left, return the player as the winner
        if(len(self.players) == 1):
            return self.players[0]

        # By default return none if no player won the game in this round
        return None

    # Remove all players in to_remove list of player instances
    def remove_players(self, to_remove):
        for player in to_remove:
            print(
                "{} ran out of cards and is out of the game!".format(
                    player.name))
            self.players.remove(player)
