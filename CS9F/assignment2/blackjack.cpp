#include <iostream>
#include "cards.h"
#include "hands.h"

using namespace std;

// You complete this function, which takes two hands and a deck as arguments. 
// It returns the result of dealing two cards each to the dealer hand and 
// the customer hand arguments.  The first card in the deck argument goes 
// to the customer, the second to the dealer, the third to the customer,
// and the fourth to the dealer. DealFirstFourCards should also print
// appropriate debugging output.
void DealFirstFourCards (DealerHand dh, CustomerHand ch, Deck d) {
	
	Card card1 = d.Deal();  
	Card card2 = d.Deal();
	Card card3 = d.Deal();
	Card card4 = d.Deal();
	
	ch.AddCard(card1);
	ch.AddCard(card3);
	dh.AddCard(card2);
	dh.AddCard(card4);
	
	ch.Print();
	dh.Print();
}

// You complete this function, which takes two hands and a deck as arguments. 
// On entry, each hand has already been dealt two cards, and neither hand has 
// a blackjack (a total of 21). ResultOfPlay returns the result of playing
// the hand. 
// First, the customer draws cards until he/she either goes past 21 (a "bust") 
// or reaches a suitable total less than or equal to 21. If the customer has 
// not bust, then the dealer draws cards until reaching a total of 17 or more. 
// ResultOfPlay returns 0 if the customer busts or if the customer's total is 
// less than or equal to the dealer's and the dealer hasn't bust. 
// ResultOfPlay returns 1 if the dealer busts or if the customer's total 
// exceeds the dealer's and the customer has not bust.
// ResultOfPlay should also print appropriate debugging output.
int ResultOfPlay (DealerHand dh, CustomerHand ch, Deck d) {
    while(true) {
    
    if (ch.CanDraw(dh.UpCard())) { 
    	ch.AddCard(d.Deal());
    }
    else {
    	if(dh.CanDraw()) {
		dh.AddCard(d.Deal());
	}
	else {
		if (ch.Total() > 21 || (dh.Total() <= 21 && ch.Total() <= dh.Total())) {
			dh.Reset();
			ch.Reset();
			return 0;
		}
		else {
			dh.Reset();
			ch.Reset();
			return 1;
		}
	}
    }
    }
}

int main () {
    Deck d(true);
    int numGames, numWins;
    DealerHand dealerHand;
    CustomerHand ourHand;
    cout << "How many games? ";
    cin >> numGames;
    numWins = 0;
    for (int k=1; k<=numGames; k++) {
	DealFirstFourCards (dealerHand, ourHand, d);
	if (dealerHand.Total()==21) {
	    cout << "LOSS: Dealer has blackjack" << endl;
	} else if (ourHand.Total()==21) {
	    numWins += 2;
	    cout << "WIN:  We have blackjack" << endl;
	} else {
	    numWins += ResultOfPlay (dealerHand, ourHand, d);
	}
	d.Shuffle();
    }
    cout << "We won " << numWins << " out of " << numGames << endl;
    return 0;
}
