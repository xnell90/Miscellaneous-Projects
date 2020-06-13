package gameLogic;
import java.util.ArrayList;

public class Hand {
	
	private ArrayList<Card> hand; 
	
	public Hand() {
		this.hand = new ArrayList<Card>();
	}
	
	public void reset() {
		this.hand.clear();
	}
	
	public void add(Card card) {
		this.hand.add(card);
	}
	
	public int size() {
		return this.hand.size();
	}
	
	public int getTotalValue() {
		int totalValue = 0;
		int numAces = 0;
		
		for(Card card: this.hand) {
			switch (card.getRank()) {
			case 'A': 
				numAces += 1;
				break;
			case '2':
			case '3':
			case '4':
			case '5':
			case '6':
			case '7':
			case '8':
			case '9':
				totalValue += Character.getNumericValue(card.getRank());
				break;
			case 'K':
			case 'Q':
			case 'J':
				totalValue += 10;
				break;
			}
		}
		
		if (numAces == 1) {
			totalValue += 11;
		} else {
			totalValue += numAces;
		}
		
		return totalValue;
	}
	
	public String toString() {
		String output = " | ";
		for(Card card: this.hand) {
			output += card.getCard() + " | ";	
		}
		
		return output;
	}

}
