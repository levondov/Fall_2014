#include <iostream>
#include "dll.h"

using namespace std;

int main () {
    const int N = 8;
    const int K = 2;
    DLLnode *list = 0;
    DLLnode *last = 0;
    for (int j=N; j>0; j--) {
		DLLnode *newGuy = new DLLnode (j);
		if (j==N) {
			last = newGuy;
		}
		list = list->Insert(newGuy);
    }
    
    
    list->Print();
    while (!list->LengthIs1 ()) {
		for (int j=0; j<K; j++) {
		    list = list->Next ();
		}
		list = list = list->Delete();		
		list->Print();

    }
    
    cout << "Only one person remains: ";
    list->Print ();
    return 0;
}

