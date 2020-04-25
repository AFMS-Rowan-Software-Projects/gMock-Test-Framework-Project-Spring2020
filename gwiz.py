import sys
import argparse
from find_gMock_files import find
from mockclass_gen import create_mock_class, create_mock_class_new, parse_cpp_file
from full_file_creator import make_full_file
from runner import run_tests
from step_through_format import start_step_through_format

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

# parse args and get filename
args = parser.parse_args()
filename = args.filename

# check flags
if args.full:
    make_full_file(filename).write_to_file("MOCK_" + filename)
if args.create_from_class:
    fp = open(filename)
    create_mock_class(fp)
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
if args.show:
    find()
if args.step:
    file_obj = open(filename)
    parser = parse_cpp_file(file_obj)
    parser._parse_class()
    methods = parser.detect_methods()
    mock_class = create_mock_class_new(parser.detected_class_name, methods, write_to_disk=False)
    start_step_through_format(mock_class, methods)

