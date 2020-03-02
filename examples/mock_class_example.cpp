

class MOCK_TestClass {
public:
	MOCK_METHOD(bool, CheckOne, (bool, int, String));
	MOCK_METHOD(int, CheckTwo, (float), (override));
	MOCK_METHOD(void, DoMath, (int, int)(const));
	MOCK_METHOD(PacketStream*, Connect, (), (override, const));
};

