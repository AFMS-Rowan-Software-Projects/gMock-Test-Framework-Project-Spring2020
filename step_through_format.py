# user runs command and gives class to be mocked
# have user name test suite
# mock the class
# build boilerplate test suite
# loop through mocked class' methods and insert statements

from cpp_gen import CppFile, Function, MacroFunction


def start_step_through_format(mock_class, methods):
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
            create_test(test_suite_name, test_name)

    # end with creating main function and write to file


def create_test(test_suite_name, test_name):
    test_one = MacroFunction('TEST', test_suite_name, test_name)
