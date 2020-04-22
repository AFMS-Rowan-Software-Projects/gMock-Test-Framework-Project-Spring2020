import sys
import argparse
from mockclass_gen import create_mock_class_from_file
from full_file_creator import make_full_file
from runner import run_tests
import sys

# debug
print(sys.argv)
gtest_args = [a for a in sys.argv if a.startswith('--lgtest')]
sys.argv = [a for a in sys.argv if not a.startswith('--lgtest')]
print('args: {}'.format(sys.argv))
print('gtest args: {}'.format(gtest_args))

# setup flag parser
parser = argparse.ArgumentParser()

# add flags to flag parser
parser.add_argument('filename', type=str, required=False)
# run options
run_options = parser.add_mutually_exclusive_group(required=False)
run_options.add_argument('-f', '--full', action='store_true', help="run full file creator")
run_options.add_argument('-r', '--run', action='store_true', help="run all tests")
run_options.add_argument('-t', '--test', type=str, help="run the specified test suite")
run_options.add_argument('-s', '--subtest', type=str, nargs=2, help="run the specified subtest of the test suite")

# parse args and get filename
args = parser.parse_args()
filename = args.filename

# check flags
if args.full:
    make_full_file(filename).write_to_file("MOCK_" + filename)
else:
    fp = open(filename)
    mock_class_file = create_mock_class_from_file(fp)
if args.run:
    test = None
    subtest = None
    run_tests(filename, test, subtest)
if args.test:
    test = args.test
    subtest = None
    print(args.test)
    run_tests(filename, test, subtest)
if args.subtest:
    subtestArgs = args.subtest
    test = subtestArgs[0]
    subtest = subtestArgs[1]
    print(subtestArgs)
    run_tests(filename, test, subtest)
