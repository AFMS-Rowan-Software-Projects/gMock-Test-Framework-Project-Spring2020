#include <iostream>
#include "Shape.cpp"
using namespace std;

class Rectangle : public Shape {
  public:
    void set_values(unsigned int x, int y) {
        width = x;
        height = y;
    }
    int getArea() {return width*height;}
};

int square(int i)
{
    return i * i;
}
