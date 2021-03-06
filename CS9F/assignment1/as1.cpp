#include <iostream>
#include <string>
using namespace std;

// Number adding program
// simply adds numbers and displays totals
int main() {
	
	int overall_total = 0;
	int current_total = 0;
	int current_input = -1; // -1 and not 0 otherwise the program will terminate if the first input is a 0
	int previous_input;

	cout << "\n Welcome to the adding simulating machine! \n" << endl;
	
	while (true) {
		previous_input = current_input;
		cin >> current_input;
		current_total += current_input;
		overall_total += current_input;
		if (current_input == 0 && previous_input == 0) {
			break;
		}
		else if (current_input == 0) {
			cout << "Subtotal = " << current_total << endl;
			current_total = 0;
		}
	}
	cout << "Total = " << overall_total << endl;
}

