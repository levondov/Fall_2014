#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

int main() {
int myarray [2] = {};

cout << myarray[1] << endl;

myarray[1] = 4;

cout << myarray[1] << endl;

myarray[2] = 3;

cout << myarray[2] << endl;

for (int i = 0; i < 10; i++) {
cout << i << endl;
}
int alist [4] = {1,2,3,4};
if (1 == 1 && 2 == 2) {
cout << alist[1] << endl;
int a = 3;
int * b;
b = &a; // b = address of a	
*b = 10; // change whatever b is pointed to 
cout << a << endl;
int total = 5;
int sum = 3;
total = sum;
cout << total << endl;
}
}

