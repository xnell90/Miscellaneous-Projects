# Blackjack

<p align = 'justify'>
Blackjack is a comparing card game between usuallly several players and dealers, where each player in turn competes against the dealer.
It is played with one or more decks of 52, and is the most widely played casino banking game in the world. The objective of the game is
to beat the dealer in one of the following ways:
</p>

 * Get 21 points on the player's first two cards, without a dealer blackjack;
 * Reach a final score higher than the dealer without exceeding 21; or
 * Let the dealer draw additional cards until their hand exceeds 21.

<p align = 'justify'>
Players are each dealt two cards, face up or down depending on the casino and the table at which you sit. The value of cards two through ten is their pip value (2 through 10). Face cards (Jack, Queen, and King) are all worth ten. Aces can be worth one or eleven. A hand's value is the sum of the card values. Players are allowed to draw additional cards to improve their hands. A hand with an ace valued as 11 is called "soft", meaning that the hand will not bust by taking an additional card; the value of the ace will become one to prevent the hand from exceeding 21. Otherwise, the hand is "hard".
</p>

After receiving an initial two cards, the player has up to four standard options: "hit", "stand", "double down", or "split". 

***Hit***: Take another card from the dealer.

***Stand***: Take no more cards.
 
<p align = 'justify'>
<i><b>Double down</b></i>: The player is allowed to increase the initial bet by up to 100% in exchange for committing to stand after receiving    exactly one more card. The additional bet is placed in the betting box next to the original bet. 
</p>
 
<p align = 'justify'>
<i><b>Split</b></i>: If the first two cards of a hand have the same value, the player can split them into two hands, by moving a second bet equal to the first into an area outside the betting box. The dealer separates the two cards and draws an additional card on each, placing one bet with each hand. The player then plays out the two separate hands in turn; except for a few restrictions, the hands are treated as independent new hands, with the player winning or losing their wager separately for each hand.
</p>

<p align = 'justify'>
Once all the players have completed their hands, it is the dealer’s turn. The dealer hand will not be completed if all players have either busted or received blackjacks. The dealer then reveals the hidden card and must hit until the cards total 17 or more points. (At most tables the dealer also hits on a "soft" 17, i.e. a hand containing an ace and one or more other cards totaling six.) Players win by not busting and having a total higher than the dealer, or not busting and having the dealer bust, or getting a blackjack without the dealer getting a blackjack. If the player and dealer have the same total (not counting blackjacks), this is called a "push", and the player typically does not win or lose money on that hand. Otherwise, the dealer wins. (Source: Wikipedia)
</p>


### Simulation For Our Modified Blackjack Game

<p align = 'justify'>
Imagine that there is a game of Blackjack where you have one dealer and one player. They are playing only one round of the game. The deck has 52 cards, and the Dealer draws out cards from the deck; two cards for the player and two cards for the dealer. Let's suppose that both player and dealer do not know each others hand so, by the rules of blackjack, the player must make a move. Assume that the player decided the make multiple hits until his hand value is 16 or over, and then stand. How likely will the player win the round given that the dealer only makes multiple hits until his hand value is 17 or over? 
</p>

---
### How to run the Java project?

<p align = 'justify'>
To run the Java Project, you can download the src folder and bin folder. Open Eclipse and load the project into your workspace. From there you can just run the project.
</p>

---

### Results

<p align = 'justify'>
After running the simulation for 50000 first rounds, the player has an approximate 44% chance of winning the first round while the dealer has an approximate 46% chance of winning the first round. This means that there is an approximate 10% chance of having a push on the first round. Based on this we can conclude that one the first round, if the player decides to hit until the hand value is above 16, the dealer will on average win the first round.
</p>

