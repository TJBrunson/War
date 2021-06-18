# War

### -- Requirements --
1. choose number of opponents (maximum 3)
2. shuffle deck of cards, and split between number of players
3. user types 'draw' to start a round which pops card from each player
4. cards are compared
5. return which player wins and add cards to the bottom of their deck
6. on draw, all players put down 3 cards or 1 - cards left in hand
    1. repeat until not a tie
7. announce winner by name

### -- Assumptions --
1. No more than 3 computers will play against the user
2. All suits are worth the same
3. If there is a tie and one player doesnt have 4 cards, they bet all but one card and use their
final card as the tie breaker. If that is still a tie, the player that is out of cards loses becasue he
ran out of cards.
4. If number of players not divisible by 52, add remainder of cards to first winner's pile

### -- Tests --
1. Check that deck builds correctly
2. Check that after dealing, each player has the same number of cards
    1. Check that left over cards are added to tie_pile