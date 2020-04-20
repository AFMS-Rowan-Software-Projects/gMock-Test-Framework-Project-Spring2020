/*
Account.cpp - A basic bank account structure with credit and debit options

Author: Thomas Schofield
Class:  Principles of Data Structures Section 2
Due:    2/14/2019
*/

#include "pch.h"
#include <iostream>
#include <iomanip>
#include <cassert>
#include <string>
#include "Account.h"

using namespace std;

namespace account_ts
{
	Account::Account() // Default constructor
	{
		accountNumber = 00000000;
		balance = 0.0;
	}

	Account::Account(int id, double amount) // Custom constructor
	{
		assert(id >= 00000000 && id <= 99999999);
		accountNumber = id;
		balance = amount;
	}

	void Account::credit(double amount)
	{
		assert(amount >= 0.00);
		balance += amount;
	}

	void Account::debit(double amount)
	{
		assert(amount >= 0.00);
		if (balance >= 0.01 && balance >= amount)
		{
			balance -= amount;
		}
		else
		{
			cout << "Amount withdrawn excedes the current balance!" << endl;
		}
	}

	void Account::print() const
	{
		cout << setprecision(2) << setfill('0');
		cout << "Account #: " << setw(8) << accountNumber << ", Balance = $" << setprecision(2) << fixed << balance << endl;
	}
}
