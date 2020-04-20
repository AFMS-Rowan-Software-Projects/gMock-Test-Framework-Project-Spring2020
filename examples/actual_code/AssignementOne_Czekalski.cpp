#include <iostream>
#include <string>
#include <sstream>

using namespace std;

//Runs the game.
void runGame();

//Prints an introduction to the console.
void printIntroduction();

//Prints the game's rule to the console.
void printAnswer();

//Sets the passed in integers to -1.
//Precondition: a, b, c are integers.
void resetNumbers(int& a, int& b, int& c);

//Evaluates the passed in integers to see if they conform to the rule.
//Precondition: a, b, and c are integers.
//Postcondition: Returns true if a, b, and c conform to the rule. Otherwise returns false.
bool evaluateRule(int a, int b, int c);

//Parses the passed in 'input' string for three integers, and sets the passed into integers to the found integers.
//Precondition: input must be a string and a, b, and c must be integers.
//Postcondition: Returns true if the three integers were succesfully set, otherwise returns false.
bool getNumbers(string input, int& a, int& b, int& c);

//Evaluates the passed in numbers to see if they are greater than -1.
//Precondition: a, b, and c must be integers.
//Postcondition: Returns true if a, b, and c are greater than -1, otherwise returns false.
bool areNumbersSet(int a, int b, int c);

int main()
{
	runGame();
	return 0;
}

void runGame()
{
	bool isRunning = true;

	string input;

	int num1;
	int num2;
	int num3;

	printIntroduction();

	while (isRunning)
	{
		//Resets the numbers to negative -1 each iteration.
		resetNumbers(num1, num2, num3);

		//Gets the input from the user.
		cout << "Enter guess: ";
		getline(cin, input);

		//Checks if the input contains the string 'quit'.
		//If it does the loop is terminated.
		if (input.find("quit") != string::npos)
		{
			isRunning = false;
		}
		else if (input.find("answer") != string::npos)
		{
			//Checks if the input contains the string 'answer'.
			//If it does the answer is printed to the console.
			printAnswer();
		}
		else
		{
			//Gets the first three numbers out of the input string, and returns
			//true if all of them are not equal to negative one.
			if (getNumbers(input, num1, num2, num3))
			{
				//Evaluates the passed in numbers to see if they conform to the rule.
				//If they do print 'Yes!', else print 'No.'
				if (evaluateRule(num1, num2, num3))
				{
					cout << "Yes!" << endl << endl;
				}
				else
				{
					cout << "No." << endl << endl;
				}
			}
			else
			{
				cout << "Invalid input: Please input three numbers, 'answer', or 'quit' to stop playing." << endl << endl;
			}
		}
	}
}

void printIntroduction()
{
	cout << endl;
	cout << "Welcome to the Guessing Game!" << endl;
	cout << "================================================================================================" << endl << endl;
	cout << " Consider this pattern: 36, 108, 324." << endl << endl;
	cout << " Please input three integers to try and uncover the hidden rule that matches the above pattern." << endl << endl;
	cout << " When you are sure you know the rule type 'answer' to see if you're correct." << endl << endl;
	cout << " If you give up, type 'quit'." << endl << endl;
	cout << "================================================================================================" << endl << endl;
}

void printAnswer()
{
	cout << "The rule is each number, except the first, must equal the previous number mulitipled by three." << endl;
	cout << "For example: 3, 9, and 27." << endl << endl;
}

bool getNumbers(string input, int& a, int& b, int& c)
{
	int counter = 1;

	stringstream stream(input);
	string num;

	//Iterate over each word in the string.
	while (stream >> num)
	{
		//Try to convert word to integer and assign to correct
		//variable. Catches invalid argument exception if non-integer
		//input is provided.
		try
		{
			if (counter == 1)
			{
				a = stoi(num);
			}
			else if (counter == 2)
			{
				b = stoi(num);
			}
			else if (counter == 3)
			{
				c = stoi(num);
			}
		}
		catch (invalid_argument)
		{	
			return false;
		}	

		counter++;
	}

	return areNumbersSet(a, b, c);
}

void resetNumbers(int& a, int& b, int& c)
{
	a = -1;
	b = -1;
	c = -1;
}

bool areNumbersSet(int a, int b, int c)
{
	if (a > -1 && b > -1 && c > -1)
	{
		return true;
	}

	return false;
}

bool evaluateRule(int a, int b, int c)
{
	if (b == (a * 3) && c == (b * 3))
	{
		return true;
	}

	return false;
}