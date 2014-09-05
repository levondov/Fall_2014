#include <iostream>
#include <string>
using namespace std;

void Head(string Person)
{
	cout << " |||||||||||||||| " << endl;
	cout << " |              | " << endl;
	cout << " |   o     o    | " << endl;
	cout << "_|              |_ " << endl;
	cout << " |  _        _  |" << endl;
	cout << " |   |______|   | " << endl;
	cout << " |              | " << endl;
	cout << Person << endl;
}

int main()
{
	Head("levon");
	return 0;
}
