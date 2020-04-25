#pragma once

//defines Polygon interface
class Polygon {
protected:
	int height;
	int width;

public:
	//virtual functions to be implemented
	virtual int getArea() = 0;

	//getters and setters
	virtual int getHeight() = 0;

	virtual void setHeight(int h) = 0;

	virtual int getWidth() = 0;

	virtual void setWidth(int w) = 0;
};