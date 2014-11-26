#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include "21game.h"
#include "players.h"
#include "cards.h"
using namespace std;


Dealer::Dealer(string name): Player(name) {
}


bool Dealer::IsStillDrawing (Card c) {
	return this->Total() <= 16;
}

Card Dealer::Upcard() {
	return myHand[0];
}

Smarter::Smarter(string name): Player(name) {
}


bool Smarter::IsStillDrawing (Card dealerUpCard) {
	if ((this->Total() < 17 && (dealerUpCard.Value() == 7 || dealerUpCard.Value() == 8 || dealerUpCard.Value() == 9 || dealerUpCard.Value() == 10 || dealerUpCard.Value() == 11)) || (this->Total() < 12 && (dealerUpCard.Value() == 2 || dealerUpCard.Value() == 3 || dealerUpCard.Value() == 4 || dealerUpCard.Value() == 5 || dealerUpCard.Value() == 6))) {
	return true;
	}
	return false;
}

OneMoreTaker::OneMoreTaker(string name): Player(name) {
	bool onemorecard = false;
}

// if according to dealer strategy, we should stop, and have not taken an extra card, then return true.
// if we have not yet hit the dealer stop strategy, keep drawing.
// if we hit dealer stop strategy and already drew our extra card, stop drawing.
bool OneMoreTaker::IsStillDrawing (Card c) {
	if ((this->Total() > 16) && !onemorecard) {
		onemorecard = true;
		return true;
	} else if (this->Total() <= 16) {
		return true;
	} else {
		return false;
	}
}

void OneMoreTaker::Reset() {
	this->Player::Reset();
	onemorecard = false;
}
