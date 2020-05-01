#include <string>
#include "Living_Being.cpp"

class Intelligent_Creature : public Living_Being  {
   protected:
        int doMath(unsigned int n, int x)
	{
		return 2*n*x + n*n + x*x;
	}
   private:
	string doDumbStuff(string s)
	{
		return "uhhhh " + s;
	}
};
