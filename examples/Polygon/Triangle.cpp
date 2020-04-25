#include "Polygon.h"

class Triangle : public Polygon {
public:
	Triangle(int h, int w) {
		height = h;
		width = w;
	}

	int getArea() {
		return (width * height) / 2;
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