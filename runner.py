import subprocess
import platform
import re


totalRegex = re.compile(r'\[==========\] Running [0-9]+ tests')
passedRegex = re.compile(r'\[  PASSED  \] [0-9]+ tests')
numRegex = re.compile(r'[0-9]+')


def run_tests(filename, testname=None, subtestname=None):
    sys = platform.system()
    process = None
    temp = filename
    if sys == "Windows":
        print("Does not work on windows yet.")
    elif sys == "Darwin":
        print("Does not work on MAC yet.")
    elif sys == "Linux" or sys == "Unix":
        # if the file name has a .cpp, then compile, if not, just run it
        if filename.endswith('.cpp'):
            subprocess.call(["g++", filename, "-orun_tests", "-lgtest", "-lgtest_main", "-pthread"])
            temp = "run_tests"
        if testname is None:
            process = subprocess.check_output("./{}".format(temp))
            subprocess.call("./{}".format(temp))
        else:
            if subtestname is None:
                process = subprocess.check_output(["./{}".format(temp), "--gtest_filter={}.*".format(testname)])
                subprocess.call(["./{}".format(temp), "--gtest_filter={}.*".format(testname)])
            else:
                process = subprocess.check_output(["./{}".format(temp), "--gtest_filter={}.{}*".format(testname, subtestname)])
                subprocess.call(["./{}".format(temp), "--gtest_filter={}.{}*".format(testname, subtestname)])
        get_basic_stats(process)
    else:
        print("Does not work on your system.")


def get_basic_stats(results):
    total = int(numRegex.search(totalRegex.search(str(results)).group()).group())
    passed = int(numRegex.search(passedRegex.search(str(results)).group()).group())
    if total == 0:
        percent = 100;
    else:
        percent = (passed / total) * 100
    print("{}/{} ({}%) of the tests passed.".format(passed, total, percent))

