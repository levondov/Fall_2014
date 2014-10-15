#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <cctype>
#include <string>
#include <stdlib.h>
#include <vector>
#include "inventory.h"

using namespace std;


void InterpretCommands (istream&, Inventory& donated_items);
void InterpretUpdate (istream&, Inventory& donated_items);
void InterpretList (istream&, Inventory& donated_items);
void InterpretBatch (istream&, Inventory& donated_items);
void InterpretQuit (istream&);

void InterpretBatch (istream& lineIn, Inventory& donated_items) {
  	ifstream myfile;	
  	string filename;
  	string lineInFile;
  	string lineInWord;
	

  	if ((lineIn >> filename).fail()) {
  		cout << "***Error, make sure the number of arguments and the argument types are correct." << endl;
  	} else { 
  	  	myfile.open(filename.c_str());
  		if (myfile.fail() ) {
  			cout << "***Error, could not open file, try again." << endl;
  		} else {
  	
  			while (getline(myfile,lineInFile)) {
  				istringstream lineInFileIS  (lineInFile.c_str());
  				if (!(lineInFileIS >> lineInWord)) {
      			// if the user entered nothing, just blanks.
		 	     cerr << "***Error, no input recognized, try again." << endl;
    			} else if (lineInWord=="update") {
      				InterpretUpdate (lineInFileIS, donated_items);
		 	    } else if (lineInWord=="list") {
   		 	     	InterpretList (lineInFileIS,donated_items);
		 	    } else if (lineInWord=="batch") {
		  	    	InterpretBatch (lineInFileIS, donated_items);
    			} else if (lineInWord=="quit") {
      				InterpretQuit (lineInFileIS);
    			} else { 
      				cerr << "***Error, unrecognizable command word." << endl; 
    			}		
			}
		}
	}
}
void InterpretUpdate (istream& lineIn, Inventory& donated_items) {
	string word;
	string extrawords;
	int num;
	// check for all possible error
	// these include: not enough arguments and wrong object types
	if ((lineIn >> word).fail() || (lineIn >> num).fail() || atoi(word.c_str()) || !(lineIn >> extrawords).fail()) { 
		cerr << "***Error, make sure the number of arguments and the argument types are correct." << endl;	
	} else {
		donated_items.Update(word,num);
	}

	

}
void InterpretList (istream& lineIn, Inventory& donated_items) {
	string list_type,extra_words;
	
	if ((lineIn >> list_type).fail()) { // check to see if an argument was given.
		cerr << "***Error, make sure the number of arguments and the argument types are correct." << endl;
	} else {
		if (!((lineIn >> extra_words).fail())) { // too many arguments
			cerr << "***Error, make sure the number of arguments and the argument types are correct." << endl;
		} else { // check to see if user wants quantities or names
			string compare_string = "names";
			string compare_string2 = "quantities";
			if (!(list_type.compare(compare_string))) { 
				cout << endl;
				donated_items.ListByName();
				cout << endl;
			} else if (!(list_type.compare(compare_string2))) {
				cout << endl;
				donated_items.ListByQuantity();
				cout << endl;
			} else {
				cerr << "***Error, you spelled a command incorrectly, try again" << endl;
			}
		
		}
	}
}

void InterpretQuit (istream& lineIn) {
	exit(1);
}

void InterpretCommands (istream& cmds, Inventory& donated_items) {
  string line, lineInWord;
  while (getline(cin,line)) {
  
    istringstream lineIn (line.c_str());
    if (!(lineIn >> lineInWord)) {
      // if the user entered nothing, just blanks.
      cerr << "Error, no input recognized, try again." << endl;
    } else if (lineInWord=="update") {
      InterpretUpdate (lineIn, donated_items);
    } else if (lineInWord=="list") {
      InterpretList (lineIn, donated_items);
    } else if (lineInWord=="batch") {
      InterpretBatch (lineIn, donated_items);
    } else if (lineInWord=="quit") {
      InterpretQuit (lineIn);
    } else { 
      cerr << "Error, unrecognizable command word." << endl; 
    }
  }
}

int main ( ) {
	Inventory donated_items;
	cout << "******* WELCOME TO THE DONATED INVENTORY LIST *******" << endl;
	cout << "What do you want to do? (batch, update, list names, list quantities)" << endl;
  	InterpretCommands (cin, donated_items);
  	return 0;
}
