import sys
from runner import run_tests

filename = sys.argv[1]
test = None
subtest = None
if len(sys.argv) > 2:
    test = sys.argv[2]
if len(sys.argv) > 3:
    subtest = sys.argv[3]

run_tests(filename, test, subtest)