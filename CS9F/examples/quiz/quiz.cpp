#include <iostream>
#include <iomanip> // for setw
#include <string>
using namespace std;
#include "randgen" // for RandInt
#include "prompt"


int MakeQuestion() {
// postcondition: creates a random question, returns the answer

	const WIDTH = 7;
	RandGen gen;
	int num1 = gen.RandInt(10,20);
	int num2 = gen.RandInt(10,20);
	cout << setw(WIDTH) << num1 << endl;
	cout << "+" << setw(WIDTH−1) << num2 << endl;
	cout << "——-" << endl;
	return num1 + num2;
	
	}
	
int main() {
	string name = PromptString("what is your name? ");
	int correctCount = 0;
	int total = PromptRange(name + ", how many questions, ",1,10);
	int answer,response, k;
	for(k=0; k < total; k++) { 
		answer = MakeQuestion();
		cout << "answer here: ";
		cin >> response;
		if (response == answer) { 
			cout << "correct! " << endl;
			correctCount++;
			}
		else { 
			cout << "incorrect, answer = " << answer << endl;
			}
	}
	int percent = double(correctCount)/total ∗ 100;
	cout << name << ", your score is " << percent << "%" << endl;
	return 0;
}



