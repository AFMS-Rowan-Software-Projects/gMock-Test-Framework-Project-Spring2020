from mockclass_gen import MockClass

mc = MockClass("TestClass")

mc.add_mock_method("bool", "CheckOne", ["bool", "int", "String"], virtual=False, const=False)
mc.add_mock_method("int", "CheckTwo", ["float"], virtual=True, const=False)
mc.add_mock_method("void", "DoMath", ["int", "int"], virtual=False, const=True)
mc.add_mock_method("PacketStream*", "Connect", [], virtual=True, const=True)

print(mc.generate())