#include <vector>
#include <string>
#include <iostream>
#include <sstream>

class Inventory {
public:
	Inventory ();
	void Update (string item, int amount);
	void ListByName ();
	void ListByQuantity ();
private:
	vector<struct> inventory; 
	
};
