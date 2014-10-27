#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <cctype>
#include <string>
#include <stdlib.h>
#include <vector>

using namespace std;


int main ( ) {
	const int k = 0;
	for (int* i = k; k != 10; i=k) {
	cout << i << endl;
	delete i;
	cout << i << endl;
	}
	
  	return 0;
}
