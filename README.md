# War

# -- Usage --
1. main_algorithm.py will run the game algorithmically with 3 players.
2. main.py allows users to choose the number of players and a name for each player. Users also hit enter to play a round.

# -- Requirements --
1. Choose number of players(maximum 4)
2. Shuffle deck of cards, and deal to players
4. Cards are compared
5. Return which player wins and add cards to the bottom of their hand
6. On tie, all players put down 3 cards or 1 - cards left in hand
1. Repeat until not a tie
7. Announce winner by name

# -- Assumptions --
1. No more than 3 computers will play against the user
2. All suits are worth the same
3. If there is a tie and one player doesnt have 4 cards, they bet all but one card and use their
final card as the tie breaker. If that is still a tie, the player that is out of cards loses becasue he
ran out of cards.
4. If number of players not divisible by 52, add remainder of cards to first winner's pile
5. If a player cannot play in a tie breaker or runs out of cards, remove them from player pool to shorten loop runs
6. The game always has at least 1 player with cards
7. There are always 52 cards in the game.
