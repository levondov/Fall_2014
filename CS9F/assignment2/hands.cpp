#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include "hands.h"

using namespace std;

DealerHand::Dealerhand () {
	Card myUpCard;
	myCardCount = 0;
	myAceAs11Count = 0;
	myTotal = 0;
}

void DealerHand::Reset () {
	Card myUpCard;
	myCardCount = 0;
	myAceAs11Count = 0;
	myTotal = 0;
}

void DealerHand::AddCard (Card c) {
	if (myTotal == 0) {
		myUpCard = c;
	}
	
	int cardValue = c.Value();
	
	if (cardValue == 11 && myTotal + cardValue > 21) {
		myTotal++;
		myCardCount++;
	}
	else {
		myTotal += cardValue;
		myCardCount++;
		if (cardValue == 11) {
			myAceAs11Count++;
		}
	}
}

bool DealerHand::CanDraw () {
	return myTotal <= 16;
}

Card DealerHand::UpCard () {
	return myUpCard;
}

int DealerHand::Total () {
	return myTotal;
}

void DealerHand::Print () {
	cout << "Dealer Hand: "<< myCardCount <<" cards, up card = " << myUpCard.Name << ", total = "<< Total() << endl;
}

CustomerHand::CustomerHand () {
	myCardCount = 0;
	myAceAs11Count = 0;
	myTotal = 0;
}

void CustomerHand::Reset () {
	myCardCount = 0;
	myAceAs11Count = 0;
	myTotal = 0;
}

void CustomerHand::AddCard (Card c) {
	int cardValue = c.Value();
	if (cardValue == 11 && myTotal + cardValue > 21) {
		myTotal++;
		myCardCount++;
	}
	else {
		myTotal += cardValue;
		myCardCount++;
		if (cardValue == 11) {
			myAceAs11Count++;
		}
	}
}

bool CustomerHand::CanDraw (Card dealerUpCard) {
	if ((Total() < 17 && (dealerUpCard.Value() == 7 || dealerUpCard.Value() == 8 || dealerUpCard.Value() == 9 || dealerUpCard.Value() == 10 || dealerUpCard.Value() == 11)) || (Total() <12 && (dealerUpCard.Value() == 2 || dealerUpCard.Value() == 3 || dealerUpCard.Value() == 4 || dealerUpCard.Value() == 5 || dealerUpCard.Value() == 6))) {
	return true;
	}
	return false;
}

int CustomerHand::Total () {
	return myTotal;
}

void CustomerHand::Print () {
	cout << "Customer Hand: " << myCardCount " cards, total = "<< myTotal << endl;
}



