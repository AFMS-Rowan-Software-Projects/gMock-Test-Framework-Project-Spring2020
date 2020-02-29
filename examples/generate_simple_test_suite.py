from cpp_gen import CppFile, Function, MacroFunction

cpp = CppFile()

# add includes
cpp.add_include('iostream')
cpp.add_include('gtest/gtest.h')
cpp.add_namespace('std')

# test definition
test_one = MacroFunction('TEST', 'MyTestSuite', 'TestOne')
test_one.add_assert_eq(1, 1)

# main function definition
main_function = Function('int', 'main', 'int argc', 'char **argv')
main_function.add_function_call('InitGoogleTest', '&argc', 'argv',
                                namespace='testing')
main_function.add_run_all_tests_and_return()

# add methods
cpp.add_component(test_one)
cpp.add_component(main_function)
cpp.write_to_file('simple_test_suite')
