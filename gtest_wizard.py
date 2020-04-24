from cpp_gen import MacroFunction, CppClass


def create_test(test_suite, test_name):
    test = MacroFunction('TEST', test_suite, test_name)
    test.add_comment('Arrange', newline=True)
    test.add_comment('Act', newline=True)
    test.add_comment('Assert', newline=True)

    return test.generate()


def create_mock_class_boilerplate(class_to_mock):
    mock_class_name = 'Mock' + class_to_mock
    mock_class = CppClass(mock_class_name, base_class=class_to_mock)
    mock_class_public = mock_class.add_public_specifier()
    mock_class_public.add_comment('Put mock methods here')

    return mock_class.generate()


print(create_test('MyTestSuite', 'MyTest'))
# output:

# TEST(MyTestSuite, MyTest) {
# 	// Arrange
#
# 	// Act
#
# 	// Assert
#
# }

print(create_mock_class_boilerplate('Turtle'))
# output:

# class MockTurtle : public Turtle {
# public:
# 	// Put mock methods here
# };

