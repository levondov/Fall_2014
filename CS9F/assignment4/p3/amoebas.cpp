#include "amoebas.h"
#include <string>
#include <iostream>

using namespace std;

Amoeba::Amoeba (string s) {	// an amoeba is born, named s
	myName = s;
	myParent = 0;
	myOlderSibling = 0;
	myOldestChild = 0;
	myYoungestChild = 0;
}

// Access functions
string Amoeba::Name () {
	return myName;
}

Amoeba* Amoeba::Parent () {
	return myParent;
}

void Amoeba::AddChild (Amoeba* newChild) {
	// make child point to parent
	newChild->myParent = this;

	// check for parent having other children
	Amoeba* otherSibling = myYoungestChild;
	if (!otherSibling) {	// the new amoeba is an only child
		myYoungestChild = newChild;	// make the parent's child
		myOldestChild = newChild;		// ptrs point to the new one
		newChild->myOlderSibling = 0;	// no older sibling
	} else {	// there are other kids; make this one the youngest
		myYoungestChild = newChild;	// no younger siblings,
		newChild->myOlderSibling = otherSibling;	// but new kid now
	}					// has older siblings.
}

void Amoeba::PrintChildren () {
	Amoeba* youngest = myYoungestChild;

	while (myYoungestChild) {
		cout << myYoungestChild->Name() << endl;
		myYoungestChild = myYoungestChild->myOlderSibling;
	}
	myYoungestChild = youngest;
}

void Amoeba::PrintGrandchildren () {
	Amoeba* youngest = myYoungestChild;
	while (myYoungestChild) {
		myYoungestChild->PrintChildren();
		myYoungestChild = myYoungestChild->myOlderSibling;
	}
	myYoungestChild = youngest;
}

void Amoeba::PrintDescendants (int spacing) {
	Amoeba* youngest = myYoungestChild;
	string blanks(spacing*4,' ');
	while(myYoungestChild) {
		
		if (myYoungestChild->myYoungestChild) {
			cout << blanks << myYoungestChild->Name() << endl;
			myYoungestChild->PrintDescendants(spacing+1);
		} else {
			cout << blanks << myYoungestChild->Name() << endl;
		}
		
		myYoungestChild = myYoungestChild->myOlderSibling;
		
	}
	
	
}
























