#include <iostream>
#include <string>
using namespace std;
// illustrates function prototypes
void Hi(string);
void Greetings();
int number;
void Hi (string name)
{
cout << "Hi " << name << endl;
Greetings();
}
void Greetings()
{
cout << "Things are happening inside this computer" << endl;
cout << "Give me a animal ";
cin >> number;
cout << number << endl;
}
int main()
{
Hi("Fred");
return 0;
}
