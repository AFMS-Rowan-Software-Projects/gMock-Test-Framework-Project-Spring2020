import sys, argparse
from find_gMock_files import find
from mockclass_gen import create_mock_class_from_file
from full_file_creator import make_full_file, make_empty_test_suite
from runner import run_tests

# pull out gtest flags
gtest_flags = [a for a in sys.argv if a.startswith('--lgtest') or a.startswith('--gtest')
            or a.startswith('--gmock')]
sys.argv = [a for a in sys.argv if a not in gtest_flags]
print('gtest_flags: {}'.format(gtest_flags))
print('flags: {}'.format(sys.argv))

# setup flag parser
parser = argparse.ArgumentParser()

# add flags to flag parser
parser.add_argument('filename', nargs='?',  type=str)
# run options
run_options = parser.add_mutually_exclusive_group(required=False)
run_options.add_argument('-f', '--full', action='store_true', help="run full file creator")
run_options.add_argument('-c', '--create_from_class', action='store_true', help="create mock class from class")
run_options.add_argument('-r', '--run', action='store_true', help="run all tests")
run_options.add_argument('-t', '--test', type=str, help="run the specified test suite")
run_options.add_argument('-s', '--subtest', type=str, nargs=2, help="run the specified subtest of the test suite")
run_options.add_argument('-l', '--show', action='store_true',  help="list all gMock files in directory")
run_options.add_argument('-step', action='store_true', help="create mock class from class using the step through "
                                                            "format")
run_options.add_argument('-S', '--create_test_suite',action='store_true', help="Create a simple test suite with one empty test per method in"
                                                         "the class.")

# parse args and get filename
args = parser.parse_args()
filename = args.filename

# check flags
if args.full:
    make_full_file(filename).write_to_file("MOCK_" + filename)
if args.create_from_class:
    fp = open(filename)
    mock_class_file = create_mock_class_from_file(fp)
if args.run:
    run_tests(filename)
if args.test:
    test = args.test
    print(args.test)
    run_tests(filename, test)
if args.subtest:
    subtestArgs = args.subtest
    test = subtestArgs[0]
    subtest = subtestArgs[1]
    print(subtestArgs)
    run_tests(filename, test, subtest)
if args.show:
    find()
if args.step:
    raise NotImplementedError()
if args.create_test_suite:
    make_empty_test_suite(filename).write_to_file("SUITE_")
