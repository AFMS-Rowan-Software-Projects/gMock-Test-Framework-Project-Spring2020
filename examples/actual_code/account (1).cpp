
#include <iostream>
#include "account.h";
using namespace std;

account::account(int acct)
{
	assert(acct > 0 && acct < 1000000000);

	accountNumber = acct;
	balance = 0;
}

account::account(int acct, double money)
{
	assert(money > 0);
	assert(acct > 0 && acct < 1000000000);

	accountNumber = acct;
	balance = money;
}

void account::debit(int input)
{
	assert(input > 0);

	if (input > balance)
	{
		cout << "\nError!\nAmount withdrawn exceeds current balance!\n";
	}
	else
	{
		balance -= input;
		cout << "Balance is ";
		printf("%.2f", balance);
	}
}

void account::credit(int input)
{
	assert(input > 0);
	balance += input;
	cout << "Balance is ";
	printf("%.2f", balance);
}

void account::print()
{
	cout << "\nA/C no: " << accountNumber << "\nBalance: " << balance;
}