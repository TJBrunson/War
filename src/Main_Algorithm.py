from models.Game import Game
from models.Player import Player

game = Game(["Tim", "Emily", "Ed"])

winner = None

while(winner == None):
    winner = game.play_round()
    
print("Congratulations {}, you won the game!".format(winner.name))