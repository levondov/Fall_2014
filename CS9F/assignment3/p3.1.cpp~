#include <iostream>
#include <fstream>
#include <sstream>
#include <cctype>
#include <string>
#include <stdlib.h> 

using namespace std;


void InterpretCommands (istream&);
void InterpretUpdate (istream&);
void InterpretList (istream&);
void InterpretBatch (istream&);
void InterpretQuit (istream&);

void InterpretBatch (istream& lineIn) {
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
      				InterpretUpdate (lineInFileIS);
		 	    } else if (lineInWord=="list") {
   		 	     	InterpretList (lineInFileIS);
		 	    } else if (lineInWord=="batch") {
		  	    	InterpretBatch (lineInFileIS);
    			} else if (lineInWord=="quit") {
      				InterpretQuit (lineInFileIS);
    			} else { 
      				cerr << "***Error, unrecognizable command word." << endl; 
    			}		
			}
		}
	}
}
void InterpretUpdate (istream& lineIn) {
	string word;
	string extrawords;
	int num;
	// check for all possible error
	// these include: not enough arguments and wrong object types
	if ((lineIn >> word).fail() || (lineIn >> num).fail() || atoi(word.c_str()) || !(lineIn >> extrawords).fail()) { 
		cerr << "***Error, make sure the number of arguments and the argument types are correct." << endl;	
	} else {
		cout << "you typed: update " << word << " " << num << endl;
	}

	

}
void InterpretList (istream& lineIn) {
	string names;
	int nums = 0;
	
	if ((lineIn >> names).fail()) { // check to see if an argument was given.
		cerr << "***Error, make sure the number of arguments and the argument types are correct." << endl;
	} else {
		char c = names[0];			
		cout << "you typed: list " << names << " ";
		if (c >= '0' && c <= '9') { // if list quantities
			while (lineIn >> nums) { 
				cout << nums << " ";		
			}
			cout << endl;
			if (!(lineIn >> nums).eof()) { // check to see if end of file, or hit wrong object types
				cout << "***Error, make sure arguments are all ints or all strings." << endl;
			}	
		} else { // if list words
			while (lineIn >> names) { 
				if (atoi(names.c_str())) { // if there is an int in the list
					cout << endl;
					cout << "***Error, make sure arguments are all ints or all strings." << endl;
					break;
				}
				cout << names << " ";		
			}
			cout << endl;
		
		}
	}
}

void InterpretQuit (istream& lineIn) {
	exit(1);
}

void InterpretCommands (istream& cmds) {
  string line, lineInWord;
  while (getline(cin,line)) {
  
    istringstream lineIn (line.c_str());
    if (!(lineIn >> lineInWord)) {
      // if the user entered nothing, just blanks.
      cerr << "Error, no input recognized, try again." << endl;
    } else if (lineInWord=="update") {
      InterpretUpdate (lineIn);
    } else if (lineInWord=="list") {
      InterpretList (lineIn);
    } else if (lineInWord=="batch") {
      InterpretBatch (lineIn);
    } else if (lineInWord=="quit") {
      InterpretQuit (lineIn);
    } else { 
      cerr << "Error, unrecognizable command word." << endl; 
    }
  }
}

int main ( ) {
  InterpretCommands (cin);
  return 0;
}
