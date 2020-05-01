#include <string>
#include "Living_Being.cpp"

class Animal : public Living_Being {
   public:
	Animal(int nl) : Living_Being()
	{
		numLimbs = nl;
	}
	virtual string move() = 0;
	void grow()
	{
		height = height * 1.1;
		weight = weight * 1.2;
	}
	virtual string getFood()
	{
		return "Plants";
	}
   protected:
	int numLimbs;
};
