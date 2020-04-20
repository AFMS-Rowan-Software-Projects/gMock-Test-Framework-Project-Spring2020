#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>

using namespace std;

class Account {
private:
	double debit_balance;
	double credit_balance;
	double amount;
	string type;
public:
	Account();
	Account(double debit_balance, double credit_balance, double amount, string type);
	double credit(double balance, string type);
	double debit(double balance1, string type);
	void print(string type);
};

Account::Account() {
	debit_balance = 10000.00;
	credit_balance = 12000.00;
	amount = 0;
	type = "";
}
Account::Account(double balance1, double balance2, double amount1, string type1) {
	debit_balance = balance1;
	credit_balance = balance2;
	amount = amount1;
	type = type1;

}
double Account::credit(double balance2, string type) {
	float amount;
	credit_balance = balance2;
	if (type == "withdraw") {
		cout << "How much would you like to withdraw?" << endl;
		cin >> amount;
		credit_balance = credit_balance - amount;
	}
	else if (type == "deposit") {
		cout << "How much would you like to deposit?" << endl;
		cin >> amount;
		credit_balance = credit_balance + amount;
	}
	return credit_balance;
}
double Account::debit(double balance1, string type) {
	float amount;
	debit_balance = balance1;
	if (type == "withdraw") {
		cout << "How much would you like to withdraw?" << endl;
		cin >> amount;
		if (balance1 - amount < 0) {
			cout << "amount withdrawn exceeds current amount!" << endl;
		}
		else {
			debit_balance = debit_balance - amount;
		}
	}
	else if (type == "deposit") {
		cout << "How much would you like to deposit?" << endl;
		cin >> amount;
		debit_balance = debit_balance + amount;
	}
	return debit_balance;
}
void Account::print(string type) {
	if (type == "credit") {
		cout << "A/C no: 991234 Credit Balance = $" << credit_balance << endl;
	}
	else if (type == "debit") {
		cout << "A/C no: 991234 Debit Balance = $" << debit_balance << endl;
	}
}

int main() {
	Account acc;
	string type;
	string acc_type;
	double debit_balance = 10000.00;
	double credit_balance = 10000.00;
	bool done = false;
	while (!done) {
		cout << "Would you like to use credit, debit, or check balance? (type quit to exit program)" << endl;
		cin >> acc_type;
		if (acc_type == "credit") {
			cout << "Would you like to deposit or withdraw?" << endl;
			cin >> type;
			acc.credit(credit_balance, type);
		}
		else if (acc_type == "debit") {
			cout << "Would you like to deposit or withdraw?" << endl;
			cin >> type;
			acc.debit(debit_balance, type);
		}
		else if (acc_type == "balance") {
			cout << "What balance would you like to check?" << endl;
			cin >> acc_type;
			if (acc_type == "debit") {
				acc.print(acc_type);
			}
			else if (acc_type == "credit") {
				acc.print(acc_type);
			}
		}
		else if (acc_type == "quit") {
			break;
		}
	}
	cin.get();
	cin.get();
	return 0;
}