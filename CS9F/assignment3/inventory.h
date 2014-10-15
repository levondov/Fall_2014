#ifndef _INVENTORY
#define _INVENTORY
#include <vector>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

class Inventory {
	public:
		Inventory ();
		void Update (string item, int amount);
		void ListByName ();
		void ListByQuantity ();
	private:
		struct inventory {
			string item;
			int quantity;
		};
		
		vector<inventory> donated;

	
};
#endif
