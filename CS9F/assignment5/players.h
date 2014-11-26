#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include "21game.h"
#include "cards.h"

// Player is a superclass of dealer
class Dealer : public Player
{
	public:
		// your name
		Dealer(string name);
		// virtual function tht must be defined from player class
		virtual bool IsStillDrawing (Card c);
		// dealer upcard
		Card Upcard();
	private:
	
};

class Smarter : public Player
{
	public:
		Smarter(string name);
		virtual bool IsStillDrawing (Card c);
	private:
	
};

class OneMoreTaker : public Player
{
	public:
		OneMoreTaker(string name);
		virtual bool IsStillDrawing (Card c);
		void Reset();
	private:
		bool onemorecard;
	
};
