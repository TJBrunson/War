from game import Game
from player import Player

def main():
    game = Game(["Tim", "Emily", "Ed"])

    winner = None

    while(winner is None):
        print()
        winner = game.play_round()
        print()

    print("Congratulations {}, you won the game!".format(winner.name))

if __name__ == "__main__":
    main()