import re
from cpp_gen import MacroFunction, CppFile, Function
from cpp_parser import CPPParser, DetectedMethod
from mockclass_gen import MockClass, create_mock_class


def find_every_include(file, isfilename=True, delete_keyword=False):
    result = []
    if isfilename:
        f = open(file)
        result = re.findall(r'#include .*[">]\n', open(file).read())
        f.close()
    else:
        result = re.findall(r'#include .*[">]\n', open(file).read())
    for s in range(len(result)):
        result[s] = result[s].rstrip()
        if delete_keyword:
            result[s] = result[s].replace("#include ", "")
    return result


# This returns a MacroFunction object
def make_empty_test(test_name, sub_test_name):
    test = MacroFunction("TEST", test_name, sub_test_name)
    test.add_comment("Arrange")
    test.add_white_space(amount=2)
    test.add_comment("Act")
    test.add_white_space(amount=2)
    test.add_comment("Assert")
    test.add_white_space(amount=2)
    return test


# Returns a CppFile object, which can be used to print to console or write to a file
def make_full_file(filename, transfer_class_to_new_file=False):
    cpp = CppFile()
    file = open(filename)
    parser = CPPParser(file)
    parser.detect_methods()
    file.close()

    # Generate mock class
    mc = create_mock_class(parser)

    # Generate Tests
    for i in range(len(parser.methods)):
        cpp.add_component(make_empty_test(parser.detected_class_name, parser.methods[i].name + str(i)))


    cpp.add_include("iostream")
    cpp.add_include("gtest/gtest.h")
    cpp.add_include("\"gmock/gmock.h\"")

    # Adds class to file or includes class it came from
    # leaving this functionality out for now, can cause complications that we cannot fix yet
    # if transfer_class_to_new_file:
    #    cpp.add_component(parser)
    #    includes = find_every_include(filename, delete_keyword=True)
    #    for i in includes:
    #        if ("iostream" not in i) and ("gtest/gtest.h" not in i):
    #           cpp.add_include(i)
    # else:
    cpp.add_include("\"" + filename + "\"")

    cpp.add_component(mc.get_class())

    # Generates and adds the main for running tests, could make this a separate function
    run_tests = Function("int", "main", "int argc", "char **argv")
    run_tests.add_statement("testing::InitGoogleTest(&argc, argv)")
    run_tests.add_return("RUN_ALL_TESTS()")

    cpp.add_component(run_tests)

    return cpp
