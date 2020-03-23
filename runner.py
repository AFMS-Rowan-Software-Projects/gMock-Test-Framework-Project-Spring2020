import subprocess
import platform



def run_tests(testname = None, subtestname = None):
    sys = platform.system()
    if sys == "Windows":
        print("Does not work on windows yet.")
    elif sys == "Darwin":
        print("Does not work on MAC yet.")
    elif sys == "Linux" or sys == "Unix":
        if testname is None:
            process = subprocess.call("./run_tests")
        else:
            if subtestname is None:
                process = subprocess.call("./run_tests --gtest_filter={}.*".format(testname))
            else:
                process = subprocess.call("./run_tests --gtest_filter={}.{}*".format(testname, subtestname))
    else:
        print("Does not work on your system.")