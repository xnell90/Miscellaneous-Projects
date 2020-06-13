package gameLogic;

import java.io.FileWriter;
import java.io.IOException;

public class Blackjack {
	
	private Hand dealerHand;
	private Hand playerHand;
	private Deck deck;
	private int playerScore;
	private int dealerScore;
	
	public Blackjack() {
		reset(true);
	}
	
	public void reset(boolean newDeck) {
		if (newDeck) {
			this.playerScore = 0;
			this.dealerScore = 0;
			this.deck = new Deck();
			this.dealerHand = new Hand();
			this.playerHand = new Hand();
			
			this.deck.shuffle();
		}
	}
	
	public void deal() {
		Card card;

		for(int i = 1; i <= 2; i++) {
			card = deck.deal();
			this.playerHand.add(card);
			this.playerScore = this.playerHand.getTotalValue();
		}
		
		for(int i = 1; i <= 2; i++) {
			card = deck.deal();
			this.dealerHand.add(card);
			this.dealerScore = this.dealerHand.getTotalValue();
		}
	}
	
	public boolean playerTurn() {
		Card card;
		
		while (this.playerScore < 16) {
			card = deck.deal();
			this.playerHand.add(card);
			this.playerScore = this.playerHand.getTotalValue();
		}
		
		return (this.playerScore <= 21);

	}
	
	public boolean dealerTurn() {
		Card card;
		
		while (this.dealerScore < 17) {
			card = deck.deal();
			this.dealerHand.add(card);
			this.dealerScore = this.dealerHand.getTotalValue();
		}
		
		return (this.dealerScore <= 21)

	}
	
	public static  void main(String[] args) throws IOException {
		int playerWins = 0;
		int dealerWins = 0;
		int pushes = 0;
		
		FileWriter results = new FileWriter("results.txt");
		
		for (int i = 0; i < 50000; i++) {
			Blackjack blackjack = new Blackjack();
			
			blackjack.deal();
			boolean playerBust = !blackjack.playerTurn();
			boolean dealerBust = !blackjack.dealerTurn();
			
			results.write((i + 1) + "------------------------------------------------\n");
			if (playerBust == true && dealerBust == false) {
				results.write("Dealer Wins!\n");
				dealerWins += 1;
			} else if (playerBust == false && dealerBust == true) {
				results.write("Player Wins!\n");
				playerWins += 1;
			} else if (blackjack.playerScore > blackjack.dealerScore) {		
				results.write("Player Wins!\n");
				playerWins += 1;
			} else if (blackjack.playerScore < blackjack.dealerScore) {
				results.write("Dealer Wins!\n");
				dealerWins += 1;
			} else {
				results.write("Push!\n");
				pushes += 1;
			}
			
			results.write("Dealer Hand: " + blackjack.dealerHand.toString() + "\n");
			results.write("Player Hand: " + blackjack.playerHand.toString() + "\n");
			results.write("------------------------------------------------\n");
			
		}
		
		int totalRounds = playerWins + dealerWins + pushes;
		double playerWinPercentage = ((double)playerWins / totalRounds) * 100;
		double dealerWinPercentage = ((double)dealerWins / totalRounds) * 100;
		double pushesPercentage = ((double)pushes / totalRounds) * 100;
		
		System.out.println("---------------------------------------------------------------");
		System.out.println("Total wins by player: " + playerWins);
		System.out.println("Total wins by dealer: " + dealerWins);
		System.out.println("Total pushes: " + pushes);
		System.out.println("---------------------------------------------------------------");
		System.out.println("Player Win Percentage: " + Math.round(playerWinPercentage * 100.0) / 100.0 + "%");
		System.out.println("Dealer Win Percentage: " + Math.round(dealerWinPercentage * 100.0) / 100.0 + "%");
		System.out.println("Pushes Percentage: " + Math.round(pushesPercentage * 100.0) / 100.0 + "%");
		System.out.println("---------------------------------------------------------------");
		
		results.close();
		
	}

}
