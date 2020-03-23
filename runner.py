import subprocess
import platform


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
            subprocess.call(["g++", filename, "-o run_tests", "-lgtest", "-lgtest_main", "-pthread"])
            temp = "run_tests"
        if testname is None:
            process = subprocess.check_output("./{}".format(temp))
        else:
            if subtestname is None:
                process = subprocess.check_output(["./{}".format(temp), "--gtest_filter={}.*".format(testname)])
            else:
                process = subprocess.check_output(["./{}".format(temp), "--gtest_filter={}.{}*".format(testname, subtestname)])
    else:
        print("Does not work on your system.")


def get_basic_stats(results):
    