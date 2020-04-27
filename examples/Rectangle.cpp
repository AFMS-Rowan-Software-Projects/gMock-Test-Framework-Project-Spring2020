#include <iostream>
using namespace std;

class Rectangle {
    int width, height;
  public:
    void set_values(unsigned int x, int y) {
        width = x;
        height = y;
    }
    unsigned int area() {return width*height;}
};

int square(int i)
{
    return i * i;
}