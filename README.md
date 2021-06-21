# War
## Python version: 3.9.0

# -- Usage --
1. `python main_algorithm.py` will run the game algorithmically with 3 players.
2. `python main.py` allows users to choose the number of players and a name for each player. Users also hit enter to play a round.
3. `python -m unittest test_methods.py` runs the tests for this project

# -- Requirements --
1. Choose number of players(maximum 4)
2. Shuffle deck of cards, and deal to players
4. Cards are compared
5. Return which player wins and add cards to the bottom of their hand
6. On tie, all players put down 3 cards or 1 - cards left in hand
1. Repeat until not a tie
7. Announce winner by name

# -- Assumptions/Corner cases --
1. No more than 4 players are allowed at a time
2. All suits are worth the same
3. If there is a tie and one player doesnt have 4 cards, they bet all but one card and use their
final card as the tie breaker. If there is still a tie, the player that is out of cards loses becasue they
ran out of cards.
4. If number of players not divisible by 52, add remainder of cards in the deck to first winner's pile. This way, the winner of the first round will be awarded the remainder of the deck
5. If a player cannot play in a tie breaker or runs out of cards, remove them from player pool to shorten loop runs. This is okay because there is no way for them to rejoin the game
6. The game always has at least 1 player with cards
7. There are always 52 cards in the game.

# -- With more time I would have... --
1. implemented a gui to show the player's hands and have a button to start a round. I would have done this with tkiner to stick to a single language.
2. created a mode where users can choose to play solo against up to 3 computers who's names are randomly generated. The user's name in the game would become 'you' in the console logs and gui.
3. improved the structure of the code into an src/ file structure that worked
4. moved codes for each class into their own files and put them in a /tests/ directory.
5. made the card ranks an enum similar to how the Suits enum works.
