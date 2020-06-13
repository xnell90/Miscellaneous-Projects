package gameLogic;

public class Card {
	static final char[] ranks = {'A', '2', '3', 
								 '4', '5', '6', 
								 '7', '8', '9', 
								 'J', 'Q', 'K'};
	
	static final String[] suits = {"Hearts", "Diamonds",
								   "Spades", "Clubs"};
	private char rank;
	private String suit;
		
	public Card(char rank, String suit) {
		this.rank = rank;
		this.suit = suit;
	}
	
	public char getRank() {
		return this.rank;
	}
	
	public String getCard() {	
		return (rank + " of " + this.suit);
	}
	
}
