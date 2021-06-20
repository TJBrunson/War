import sys
from game import Game
# Function to ask user for number of players


def get_num_of_players():
    counter = 0
    while counter < 3:
        text = input()
        try:
            string_int = int(text)
            if(string_int < 5 and string_int > 1):
                return string_int
            else:
                print("Between 2 and 4 players can play at a time. Try that again...")
        except ValueError:
            counter += 1
            print("Try entering a number less than 5...")
    return None


print("Welcome to the card game War!")

# Figure out how many players the user wants
print("How many players are there? (max 4)")
num_of_players = get_num_of_players()
if num_of_players is None:
    print("You have to enter a number under 5 to start the game!")
    sys.exit()


# Choose name for each player
player_names = []
for num in range(num_of_players):
    print("Enter a name for player {}...".format(num + 1))
    name = input()
    if(name is None or name == '' or len(name) > 40):
        player_names.append("Player {}".format(num + 1))
    elif name in player_names:
        print("That name is already in use! try again...")
        num -= 1
    else:
        player_names.append(name)


# create game with players
game = Game(player_names)

winner = None

while winner is None:
    print()
    input("Press Enter to play a round...")
    print()
    winner = game.play_round()
