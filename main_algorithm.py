from game import Game
from player import Player

game = Game(["Tim", "Emily", "Ed"])

winner = None

while(winner == None):
    print()
    winner = game.play_round()
    print()
    
print("Congratulations {}, you won the game!".format(winner.name))