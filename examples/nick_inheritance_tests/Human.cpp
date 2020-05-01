#include <string>
#include "Animal.cpp"
#include "Intelligent_Creature.cpp"

class Human : public Animal, public Intelligent_Creature {
   public:
	Human(int nl, float w, double h) : Animal(nl)
	{
		weight = w;
		height = h;
	}
	string move()
	{
		return "A person walks on two legs!";
	}
	float getWeight()
	{
		return weight;
	}
	double getHeight()
	{
		return height;
	}
	virtual string getFood()
	{
		return "Plants";
	}
	string speak()
	{
		return "Hello, I am a person";
	}
};
