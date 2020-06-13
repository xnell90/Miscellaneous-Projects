package gameLogic;
import java.util.ArrayList;

public class Deck {
	
	private ArrayList<Card> deck = new ArrayList<Card>();
	
	public Deck() {
		build();
	}
	
	public void build() {
		
		for (String suit: Card.suits) {
			for (char rank: Card.ranks) {
				this.deck.add(new Card(rank, suit));
			}
		}
		
	}
	
	public Card deal() {	
		return this.deck.remove(0);
	}
	
	public void shuffle() {
		
		for(int i = 1; i <= 200; i++) {
			
			int j = (int)(this.deck.size() * Math.random());
			int k = (int)(this.deck.size() * Math.random());
			
			while (j == k) {
				j = (int)(this.deck.size() * Math.random());
				k = (int)(this.deck.size() * Math.random());
			}
			
			Card temp = this.deck.get(j);
			this.deck.set(j, this.deck.get(k));
			this.deck.set(k, temp);
			
		}
		
	}
	
}
