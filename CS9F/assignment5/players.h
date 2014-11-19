#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include "21game.h"
#include "cards.h"

class Dealer : public Player
{
	public:
		Dealer(string name);
		virtual bool IsStillDrawing (Card c);
		Card Upcard();
	private:
		Card myUpCard;
	
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