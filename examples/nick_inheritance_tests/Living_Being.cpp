#include <string>

class Living_Being {
   public:
	Living_Being()
	{
		isAlive = true;
	}
	void kill()
	{
		isAlive = false;
		std::cout << "A being was killed" << endl;
	}
	virtual float getWeight() = 0;
	virtual double getHeight() = 0;
	virtual string getFood()
	{
		return "CHEMICALS IN THE WATER";
	}
   protected:
        bool isAlive;
        float weight;
        double height;
};
