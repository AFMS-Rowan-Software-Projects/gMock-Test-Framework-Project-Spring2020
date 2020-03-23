import subprocess
import platform


def run_tests(filename, testname = None, subtestname = None):
    sys = platform.system()
    process = None
    if sys == "Windows":
        print("Does not work on windows yet.")
    elif sys == "Darwin":
        print("Does not work on MAC yet.")
    elif sys == "Linux" or sys == "Unix":
        subprocess.call("g++ -o run_tests {} -lgtest -lgtest_main -pthread".format(filename))
        if testname is None:
            process = subprocess.check_output("./run_tests")
        else:
            if subtestname is None:
                process = subprocess.check_output("./run_tests --gtest_filter={}.*".format(testname))
            else:
                process = subprocess.check_output("./run_tests --gtest_filter={}.{}*".format(testname, subtestname))
    else:
        print("Does not work on your system.")

