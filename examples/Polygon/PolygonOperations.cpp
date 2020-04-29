#include "Rectangle.cpp"
#include "Triangle.cpp"
#include <iostream>

using namespace std;

class PolygonOperations{
public:
	int Stack(Polygon *p1, Polygon *p2) {
		return p1->getHeight() + p2->getHeight();
	}

	int AvgArea(Polygon *p1, Polygon *p2) {
		return (p1->getArea() + p2->getArea()) / 2;
	}

	int maxArea(Polygon *p1, Polygon *p2) {
		int max;
		int p1Area = p1->getArea();
		int p2Area = p2->getArea();
		if (p1Area > p2Area)
			max = p1Area;
		else
			max = p2Area;
		return max;
	}

	int minArea(Polygon *p1, Polygon *p2) {
		int min;
		int p1Area = p1->getArea();
		int p2Area = p2->getArea();
		if (p1Area < p2Area)
			min = p1Area;
		else
			min = p2Area;
		return min;
	}
};

int main() {
	Rectangle r(5,2);
	Triangle t(5, 2);
	PolygonOperations po;

	int stackHeight = po.Stack(&r, &t);
	int avgArea = po.AvgArea(&r, &t);
	int maxArea = po.maxArea(&r, &t);
	int minArea = po.minArea(&r, &t);

	cout << "stack height: " << stackHeight << " average area: " << avgArea <<
		" max area: " << maxArea << " min area: " << minArea;
	return 0;
}
