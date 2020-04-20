// DataStructure_Centeno_Assignment3.cpp
// Ervin Centeno
// February 10, 2019


#include "pch.h"
#include "Account_Centeno.h"
#include <iostream>
#include <cassert>
#include <cstdlib>

using namespace std;

ACCOUNT ACC;	// Initialization of class ACCOUNT.

int main()
{	
	float debit_amount, credit_amount; // Variables for debit. credit inputs.
	char replay = 'Y';
	char select;	// Input for choice debit or credit.

	cout << "The account number is " << ACC.getID() << " and the starting balance is $"
		<< ACC.getBalance() << "." << endl;
	
	while (replay == 'Y' || replay == 'y') {
		cout << "Type D to withdraw or C to add funds:";

		while (true) {		// Loops until either D, d, C or c is typed in.
			cin >> select;
			if (cin.fail() || (select != 'D' && select != 'C' && select != 'd' && select != 'c')) {
				cin.clear();
				cout << "Type in D for Debit or C for Credit: ";

			}
			else
				break;		// Breaks loop.
		}

		if ((select == 'D') || (select == 'd')) {	// Statement to use the function debit in class ACCOUNT.
			cout << "How much do you want to withdraw: ";
			cin >> debit_amount;
			ACC.debit(debit_amount);

		}
		if ((select == 'C') || (select == 'c')) {	// Statement to use the function credit in class ACCOUNT.
			cout << "How much do you want to add: ";
			cin >> credit_amount;
			ACC.credit(credit_amount);
		}

		ACC.print();	// Prints the updated account balance.

		cout << "Would you like to make another transaction? Type Y for yes or N for no: ";
		cin >> replay;	// Breaks if replay is not Y or y.

	}

	cout << "Farewell!" << endl;

	
	EXIT_SUCCESS;
}
