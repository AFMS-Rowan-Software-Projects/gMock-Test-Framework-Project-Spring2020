#include "Polygon.h"

class Rectangle : public Polygon {
public:
	Rectangle(int h, int w) {
		height = h;
		width = w;
	}

	int getArea() {
		return (width * height);
	}

	//getters and setters
	int getHeight() {
		return height;
	}

	void setHeight(int h) {
		height = h;
	}

	int getWidth() {
		return width;
	}

	void setWidth(int w) {
		width = w;
	}
};