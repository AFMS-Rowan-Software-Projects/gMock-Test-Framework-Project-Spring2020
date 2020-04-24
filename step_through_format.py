# user runs command and gives class to be mocked
# have user name test suite
# mock the class
# build boilerplate test suite
# loop through mocked class' methods and insert statements

from cpp_gen import CppFile, Function, MacroFunction


def start_step_through_format(mock_class):
    test_suite_name = input('Enter test suite name: ')

    # start creation of file
    cpp = CppFile()

    # add includes
    cpp.add_include('iostream')
    cpp.add_include('gtest/gtest.h')

    # create a test for each method
    for m in mock_class.methods:
        print(m)

    # end with creating main function and write to file
