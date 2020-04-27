# user runs command and gives class to be mocked
# have user name test suite
# mock the class
# build boilerplate test suite
# loop through mocked class' methods and insert statements

from cpp_gen import CppFile, Function, MacroFunction


def start_step_through_format(mock_class_name, methods, filename="MyTestSuite"):
    test_suite_name = input('Enter test suite name: ')

    # start creation of file
    cpp = CppFile()

    # add includes
    cpp.add_include('iostream')
    cpp.add_include('gtest/gtest.h')
    cpp.add_include("{}.cpp".format(mock_class_name))

    # create a test for each method
    for m in methods:
        if input('Do you want to test the method {}? (y/n)'.format(m.name)) == "y":
            test_name = input("Enter name of test: ")

            test = MacroFunction('TEST', test_suite_name, test_name)
            statements = {
                'ASSERT_TRUE': test.add_assert_true,
                'ASSERT_FALSE': test.add_assert_false,
                'ASSERT_EQ': test.add_assert_eq,
                'ASSERT_NE': test.add_assert_ne,
                'ASSERT_LE': test.add_assert_le,
                'ASSERT_GT': test.add_assert_gt,
                'ASSERT_GE': test.add_assert_ge,
                'EXPECT_TRUE': test.add_expect_true,
                'EXPECT_FALSE': test.add_expect_false,
                'EXPECT_EQ': test.add_expect_eq,
                'EXPECT_NE': test.add_expect_ne,
                'EXPECT_LE': test.add_expect_le,
                'EXPECT_GT': test.add_expect_gt,
                'EXPECT_GE': test.add_expect_ge
            }

            entering_statements = True
            while entering_statements:
                print('Would you like to include any of the following statements?')
                print('Enter -1 for none of these')
                for index, k in enumerate(statements):
                    print('{}. {}'.format(index, k))
                response = int(input())
                if response == -1:
                    entering_statements = False
                else:
                    statements[list(statements.keys())[response]]()

            cpp.add_component(test)

    # end with creating main function and write to file
    main_function = Function('int', 'main', 'int argc', 'char **argv')
    main_function.add_function_call('InitGoogleTest', '&argc', 'argv',
                                    namespace='testing')
    main_function.add_run_all_tests_and_return()
    cpp.add_component(main_function)
    cpp.write_to_file(filename)

