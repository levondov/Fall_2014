#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include "gameboard.h"



using namespace std;

Gameboard::Gameboard () {
	board.resize(19);
	int k,i;
	for (k=0;k<19;k++) {
		board[k].resize(19);
		for (i=0;i<19;i++) {
			board[k][i] = '.';
		}
	}

}

void Gameboard::SetCell (int player, int row, int col, const char c) {
	if (!player) {
		board[row][col] = c;
	} else {
		board[18-row][18-col] = c;
	}

}

void Gameboard::Print (int player) {
	int k,i;
	
	for (k=0;k<19;k++) {
		for (i=0;i<19;i++) {
			if (!player) {
				cout << board[k][i];
			} else {
				cout << board[18-k][18-i];
			}
		}
		cout << endl;
	}

}











