#ifndef _GAMEBOARD
#define _GAMEBOARD
#include <vector>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

class Gameboard {
	public:
		Gameboard ();
		void SetCell (int player, int row, int col, const char c);
		void Print (int player);
	private:
		vector< vector<char> > board;


	
};
#endif
