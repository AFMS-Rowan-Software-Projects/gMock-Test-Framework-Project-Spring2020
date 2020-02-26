from cpp_gen import CppFile, Method, MacroFunction


f = CppFile()

# add includes
f.add_include('iostream')
f.add_include('gtest/gtest.h')
f.add_namespace('std')

# test definition
test_one = MacroFunction('TEST', 'MyTestSuite', 'TestOne')
test_one.add_macro_call('ASSERT_EQ', '1', '2')

# main method definition
main_method = Method('int', 'main', 'int argc', 'char **argv')
main_method.add_method_call('testing::InitGoogleTest', '&argc', 'argv')
main_method.add_return('RUN_ALL_TESTS()')

# add methods
f.add_macro_function(test_one)
f.add_method(main_method)
print(f.generate())
