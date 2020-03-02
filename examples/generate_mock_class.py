from mockclass_gen import MockClass
from cpp_gen import CppFile

cpp = CppFile()

mc = MockClass("TestClass")

mc.add_mock_method("bool", "CheckOne", ["bool", "int", "String"], virtual=False, const=False)
mc.add_mock_method("int", "CheckTwo", ["float"], virtual=True, const=False)
mc.add_mock_method("void", "DoMath", ["int", "int"], virtual=False, const=True)
mc.add_mock_method("PacketStream*", "Connect", [], virtual=True, const=True)

cpp.add_component(mc.get_class())
cpp.write_to_file('mock_class_example.cpp')

# generates:
# class MOCK_TestClass {
# public:
#   MOCK_METHOD(bool, CheckOne, (bool, int, String));
#   MOCK_METHOD(int, CheckTwo, (float), (override));
#   MOCK_METHOD(void, DoMath, (int, int)(const));
#   MOCK_METHOD(PacketStream*, Connect, (), (override, const));
# };
