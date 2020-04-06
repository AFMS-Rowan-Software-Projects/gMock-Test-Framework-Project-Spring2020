#include <iostream>
using namespace std;

class Rectangle {
    int width, height;
  public:
    void set_values (int,int) {
        width = x;
        height = y;
    }
    int area() {return width*height;}
};

int square(int i)
{
    return i * i;
}