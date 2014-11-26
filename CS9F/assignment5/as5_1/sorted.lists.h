#ifndef SORTEDLIST_H
#define SORTEDLIST_H

#include <iostream>
#include <cassert>

using namespace std;

template <class NODETYPE> class SortedList;
template <class NODETYPE> class SortedListIterator;

template <class NODETYPE>
class ListNode {
	friend class SortedList<NODETYPE>;
	friend class SortedListIterator<NODETYPE>;
public:
	ListNode (const NODETYPE &);
	NODETYPE Info ();
private:
	NODETYPE myInfo;
	ListNode* myNext;
};

template <class NODETYPE>
ListNode<NODETYPE>::ListNode (const NODETYPE &value) {
	myInfo = value;
	myNext = 0;
}

template <class NODETYPE>
NODETYPE ListNode<NODETYPE>::Info () {
	return myInfo;
}

template <class NODETYPE>
class SortedList {
	friend class SortedListIterator<NODETYPE>;
	public:
		SortedList ();
		~SortedList ();
		SortedList (const SortedList <NODETYPE> &);
		void Insert (const NODETYPE &);
		bool IsEmpty ();
		SortedList & operator=(const SortedList <NODETYPE> &);
	private:
		ListNode <NODETYPE>* myFirst;
};

template <class NODETYPE>
SortedList<NODETYPE>::SortedList() {	// constructor
	myFirst = 0;
}
template <class NODETYPE>
SortedList<NODETYPE>::~SortedList () {	// destructor
	if (!IsEmpty ()) {
		cerr << "*** in destructor, destroying: ";
		ListNode <NODETYPE>* current = myFirst;
		ListNode <NODETYPE>* temp;
		while (current != 0) {
			cerr << " " << current->myInfo;
			temp = current;
			current = current->myNext;
			delete temp;
		}
		cerr << endl;
	}
}

template <class NODETYPE>
SortedList<NODETYPE>::SortedList(const SortedList <NODETYPE> &list) {	// copy constructor
	cerr << "*** in copy constructor" << endl;
	ListNode <NODETYPE>* listCurrent = list.myFirst;
	ListNode <NODETYPE>* newCurrent = 0;
	while (listCurrent != 0) {
		ListNode <NODETYPE> *temp = new ListNode <NODETYPE> (listCurrent->Info ());
		if (newCurrent == 0) {
			myFirst = temp;
			newCurrent = myFirst;
		} else {
			newCurrent->myNext = temp;
			newCurrent = temp;
		}
		listCurrent = listCurrent->myNext;
	}
}

template <class NODETYPE>
void SortedList<NODETYPE>::Insert(const NODETYPE &value) {	// Insert
	ListNode <NODETYPE> *toInsert 
	  = new ListNode <NODETYPE> (value);
	if (IsEmpty ()) {
		myFirst = toInsert;
	} else if (value < myFirst->Info ()) {
		toInsert->myNext = myFirst;
		myFirst = toInsert;
	} else {
		ListNode <NODETYPE> *temp = myFirst;
		for (temp = myFirst; 
			  temp->myNext != 0 && temp->myNext->Info () < value; 
			  temp = temp->myNext) {
		}
		toInsert->myNext = temp->myNext;
		temp->myNext = toInsert;
	}
}

template <class NODETYPE>
bool SortedList<NODETYPE>::IsEmpty () {	// IsEmpty
	return myFirst == 0;
}

template <class NODETYPE>
SortedList<NODETYPE> & SortedList<NODETYPE>::operator=(const SortedList <NODETYPE> & list) {
	// check to see if x = x
	// return this (list on left hand side)
	if (myFirst == list.myFirst) {
		cerr << "Error, you can't do that" << endl;
		return *this;
	}
	// First delete the initial nodes
	ListNode<NODETYPE> *temp = myFirst;
	ListNode<NODETYPE> *temp2 = temp;
	while (temp->myNext != 0) {
		temp = temp->myNext;
		delete temp2;
		temp2 = temp;
	}
	
	//re-assign list's first node to myfirst and return a reference to this.
	myFirst = list.myFirst;
	return *this;
} 
// make sortedlistierator also a template of the nodetype class
template <class NODETYPE>
class SortedListIterator {
	public:
		SortedListIterator(const SortedList <NODETYPE> &);
		bool MoreRemain();
		NODETYPE Next();
	private:
			SortedList <NODETYPE> *myList;
};

template <class NODETYPE>
SortedListIterator<NODETYPE>::SortedListIterator(const SortedList <NODETYPE> & list) {
		//assign the sortedlist as mylist
		myList = new SortedList<NODETYPE>(list);
}

template <class NODETYPE>
bool SortedListIterator<NODETYPE>::MoreRemain() {
	//call mylist's isempty function (isempty is a function of sortedlist)
	return !(myList->IsEmpty());
}

template <class NODETYPE>
NODETYPE SortedListIterator<NODETYPE>::Next() {
	//first get the info from the current node
	NODETYPE info = myList->myFirst->myInfo;
	//then move to the next node
	//this can also be done by creating copies and not changing pointers
	myList->myFirst = myList->myFirst->myNext;
	return info;
}

#endif
