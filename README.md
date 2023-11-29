# Black Jack Python
This Python code implements a simple text-based version of the game Blackjack. 

## 1) deal_card function:

Generates and returns a random card from a standard deck of Blackjack cards. The cards include numbers 2 through 10 and face cards (Jack, Queen, King) with a value of 10. The Ace is considered as 11.

## 2) calculate_score function:

Takes a list of cards as input and calculates the total score.
If the sum of the cards is 21 and the player has exactly 2 cards, it returns 0, indicating a Blackjack.
If there is an Ace (11) in the cards and the sum exceeds 21, it converts the Ace to a 1 to avoid busting.

## 3) display_table function:

Prints the current state of the game, including the player's cards and total score.
If the game is over, it also displays the computer's cards and total score. Otherwise, it shows only the first card of the computer.

## 4) play_blackjack function:

Implements the main game loop.
Initializes player and computer card lists.
Deals two cards to each player.
Asks the player if they want to draw another card until they choose to stop or go over 21.
The computer draws cards until it reaches a score of 17 or higher.
Compares the final scores and determines the winner.
Asks the player if they want to play again.

## 5) compare function:

Compares the final scores of the player and computer and prints the result of the game.

## 6) play_blackjack() call at the end:

Initiates the game by calling the play_blackjack function.
The game continues to run in a loop until the player chooses not to play again. It provides a text-based interface for the player to interact with and experience a simplified version of the Blackjack game.
