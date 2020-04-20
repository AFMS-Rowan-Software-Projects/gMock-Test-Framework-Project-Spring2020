//Zhihao Lin
//Assignment 3

#include <iostream>
#include <iomanip>

using namespace std;

class Account {
        private:
        int accountNumber;
        double balance;

        public:
        Account(int acc) {
                accountNumber = acc;
                balance = 1008.68;
        }
};

void credit(double a) {
    double balance;
    balance = 1008.68;
                balance = a+balance;
cout <<" Balance=$"  << fixed << setprecision(2) << balance << endl;
        }
void debit(double a) {
    double balance;
    balance = 1008.68;
                if(a > balance) {
                        cout << "amount withdrawn exceeds the current balance!" << endl;
                }
                else{
                balance -= a;
                }
cout << " Balance=$"  << fixed << setprecision(2) << balance << endl;
}


int main() {
        Account a(991234972);
        double amount;
string type;
string selection1="credit";
string selection2="debit";
string selection3="print";
char rep = 'N';
do {
cout<<"debit or credit or print?"<<endl;
cin>>type;
if (type.compare(selection1)==0) {
        cout << endl << "Enter amount to credit: ";
        cin >> amount;
        credit(amount);
    }
    else if (type.compare(selection2)==0){
        cout << endl << "Enter amount to debit: ";
        cin >> amount;
        debit(amount);
    }
    
    else if (type.compare(selection3)==0){
        cout << "A/C no: " << 991234972 << " Balance=$"  << 1008.68 << endl;
        return 0;
    }
    else{
        cout<<"incorrect selection, debit or credit or print?"<<endl;
        }
    cout << "Do you want to continue (Y/N)?\n";
    cout << "Enter a 'Y' or an 'N' :";
    cin >> rep;
  } while ((rep == 'Y') || (rep == 'y'));
}

