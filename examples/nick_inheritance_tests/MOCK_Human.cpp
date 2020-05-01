


class MOCK_Human : public Human {
public:
	MOCK_METHOD(string, move, ());
	MOCK_METHOD(float, getWeight, ());
	MOCK_METHOD(double, getHeight, ());
	MOCK_METHOD(string, getFood, (), (override));
	MOCK_METHOD(string, speak, ());
	MOCK_METHOD(void, grow, ());
	MOCK_METHOD(void, kill, ());
	MOCK_METHOD(int, doMath, (unsigned int n, int x));
};

