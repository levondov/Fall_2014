#include <iostream>
#include "cards.h"
#include "hands.h"
#include <stdlib.h> 

using namespace std;

// You complete this function, which takes two hands and a deck as arguments. 
// It returns the result of dealing two cards each to the dealer hand and 
// the customer hand arguments.  The first card in the deck argument goes 
// to the customer, the second to the dealer, the third to the customer,
// and the fourth to the dealer. DealFirstFourCards should also print
// appropriate debugging output.
void DealFirstFourCards (DealerHand& dh, CustomerHand& ch, Deck& d) {
	//
	ch.AddCard(d.Deal());
	dh.AddCard(d.Deal());
	ch.AddCard(d.Deal());
	dh.AddCard(d.Deal());
	//
	
	// Testing special cases from hw
	
	/* total <17, dealer upcard 7,8,9,10,A
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(4);
	c2.ChangeCard(7);
	c3.ChangeCard(8); // up card
	c4.ChangeCard(10);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total =17, dealer upcard 7,8,9,10,A
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(9);
	c2.ChangeCard(6);
	c3.ChangeCard(8); // up card
	c4.ChangeCard(10);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total >17, dealer upcard 7,8,9,10,A
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(9);
	c2.ChangeCard(7);
	c3.ChangeCard(8); // up card
	c4.ChangeCard(10);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total <17, dealer upcard 2-6
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(4);
	c2.ChangeCard(7);
	c3.ChangeCard(3); // up card
	c4.ChangeCard(7);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total =17, dealer upcard 2-6
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(8);
	c2.ChangeCard(7);
	c3.ChangeCard(1); // up card
	c4.ChangeCard(10);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total >17, dealer upcard 2-6
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(11);
	c2.ChangeCard(7);
	c3.ChangeCard(4); // up card
	c4.ChangeCard(7);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	//////////////////////////////////////////////////////
	/* total <12, dealer upcard 2-6
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(4);
	c2.ChangeCard(3);
	c3.ChangeCard(2); // up card
	c4.ChangeCard(10);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total =12, dealer upcard 2-6
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(9);
	c2.ChangeCard(1);
	c3.ChangeCard(3); // up card
	c4.ChangeCard(6);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total >12, dealer upcard 2-6
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(4);
	c2.ChangeCard(8);
	c3.ChangeCard(5); // up card
	c4.ChangeCard(7);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total <12, dealer upcard 7,8,9,10,A
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(4);
	c2.ChangeCard(4);
	c3.ChangeCard(8); // up card
	c4.ChangeCard(7);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total =12, dealer upcard 7,8,9,10,A
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(4);
	c2.ChangeCard(6);
	c3.ChangeCard(6); // up card
	c4.ChangeCard(10);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
	/* total >12, dealer upcard 7,8,9,10,A
	Card c1;
	Card c2;
	Card c3;
	Card c4;

	c1.ChangeCard(5);
	c2.ChangeCard(7);
	c3.ChangeCard(9); // up card
	c4.ChangeCard(7);
	
	ch.AddCard(c1);
	ch.AddCard(c2);
	dh.AddCard(c3);
	dh.AddCard(c4);
	*/
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
int ResultOfPlay (DealerHand& dh, CustomerHand& ch, Deck& d) {
    int k = 0;
    while(true) {
    
    if (ch.CanDraw(dh.UpCard())) { 
    	ch.AddCard(d.Deal());
    }
    else {
    	if (k==0) {
    	cout << "Customer stands." << endl;
    	k++;
    	}
    	
    	if(dh.CanDraw()) {
		dh.AddCard(d.Deal());
	}
	else {
		if (ch.Total() > 21 || (dh.Total() <= 21 && ch.Total() <= dh.Total())) {
			cout << "LOSE: Customer - "<< ch.Total() << ", Dealer - "<< dh.Total() << endl;
			cout << endl;
			return 0;
		}
		else {
			cout << "WIN: Customer - "<< ch.Total() << ", Dealer - "<< dh.Total() << endl;
			cout << endl;
			return 1;
		}
	}
    }
    }
}

int main () {
    // initialize random seed for rand()
    srand (time(NULL));
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
	dealerHand.Reset();
	ourHand.Reset();
    }
    cout << "We won " << numWins << " out of " << numGames << endl;
    return 0;
}
