#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include "inventory.h"



using namespace std;

Inventory::Inventory () {

}

void Inventory::Update (string item_new, int amount) {
	bool item_exists = false;
	int item_location, k, numElts = donated.size();;
	// check to see if item exists already. the search just goes element by element
	for (k=0;k<numElts;k++) {
		if (donated[k].item == item_new) {
			item_exists = true;
			item_location = k;
		}
	}
	
	if (item_exists) {
		donated[item_location].quantity += amount;
	} else { // new item needs to be added to our list
		inventory new_item = {item_new, amount};
		donated.push_back(new_item);
	}
	
	
}

void Inventory::ListByName() {
	int i,k,loc, numElts = donated.size();
	// invariant: a[0]..a[k-1] sorted
	for(k=1; k < numElts; k++) { 
		inventory hold = donated[k];
		string holdstring = donated[k].item; // insert this element
		loc = k; // location for insertion
		// shift elements to make room for hold/a[k]
		while ((0 < loc) && (holdstring < donated[loc - 1].item)) { 
			donated[loc] = donated[loc - 1];
			loc--;
		}
		
		donated[loc] = hold;
	}
	
	//print results
	for (i=0;i<numElts;i++) {
		cout << donated[i].item << " " << donated[i].quantity << endl; 
	}
}

void Inventory::ListByQuantity () {
	int i,k,loc, numElts = donated.size();
	// invariant: a[0]..a[k-1] sorted
	for(k=1; k < numElts; k++) { 
		inventory hold = donated[k];
		int holdnum = donated[k].quantity; // insert this element
		loc = k; // location for insertion
		// shift elements to make room for hold/a[k]
		while ((0 < loc) && (holdnum < donated[loc - 1].quantity)) { 
			donated[loc] = donated[loc - 1];
			loc--;
		}
		
		donated[loc] = hold;
	}
	
	//print results
	for (i=0;i<numElts;i++) {
		cout << donated[i].item << " " << donated[i].quantity << endl; 
	}
}




