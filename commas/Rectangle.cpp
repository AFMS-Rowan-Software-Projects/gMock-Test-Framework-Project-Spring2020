#include <iostream>

using namespace std;

class Rectangle {
  public:
    void set_values(std::pair<int, int> vals, std::tuple<double, int, float> t, std::string d) {
	    v = vals;
    }
    std::pair<int, int> getVals() {return v;}

  protected:
    std::pair<int, int> v;
};

int square(int i)
{
    return i * i;
}
