# user runs command and gives class to be mocked
# have user name test suite
# mock the class
# build boilerplate test suite
# loop through mocked class' methods and insert statements

from cpp_gen import CppFile, Function, MacroFunction


def start_step_through_format(mock_class, methods, filename="MyTestSuite"):
    test_suite_name = input('Enter test suite name: ')

    # start creation of file
    cpp = CppFile()

    # add includes
    cpp.add_include('iostream')
    cpp.add_include('gtest/gtest.h')

    # create a test for each method
    for m in methods:
        if input('Do you want to test the method {}? (y/n)'.format(m.name)) == "y":
            test_name = input("Enter name of test: ")
            create_and_add_test(cpp, test_suite_name, test_name)

    # end with creating main function and write to file
    main_function = Function('int', 'main', 'int argc', 'char **argv')
    main_function.add_function_call('InitGoogleTest', '&argc', 'argv',
                                    namespace='testing')
    main_function.add_run_all_tests_and_return()
    cpp.add_component(main_function)
    cpp.write_to_file(filename)


def create_and_add_test(cpp_file_obj, test_suite_name, test_name):
    test = MacroFunction('TEST', test_suite_name, test_name)
    cpp_file_obj.add_component(test)
