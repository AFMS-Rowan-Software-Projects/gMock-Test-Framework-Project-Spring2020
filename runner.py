import subprocess, platform, re, configparser

totalRegex = re.compile(r'\[==========\] Running [0-9]+ test')
passedRegex = re.compile(r'\[  PASSED  \] [0-9]+ test')
numRegex = re.compile(r'[0-9]+')


def run_tests(filename, testname=None, subtestname=None):
    sys = platform.system()
    process = None
    temp = filename
    will_run = True
    if sys == "Windows":
        print("Does not work on windows yet.")
    elif sys == "Darwin":
        print("Does not work on MAC yet.")
    elif sys == "Linux" or sys == "Unix":
        # if the file name has a .cpp, then compile, if not, just run it
        if filename.endswith('.cpp'):
            subprocess.call(["g++", filename, "-orun_tests", "-lgtest", "-lgtest_main", "-pthread"])
            temp = "run_tests"
            will_run = assert_warning(filename, ten=testname, sten=subtestname)
        if will_run:
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


# Returns a bool, true if the amount of asserts is less than the max asserts
def assert_warning(fn, ten=r".*", sten=r".*"):
    tn = r".*"
    stn = r".*"
    if ten is not None:
        tn = ten
    if sten is not None:
        stn = sten
    f = open(fn)
    tests = re.findall(r"TEST\s*\(\s*" + tn + r"\s*,\s+" + stn + r"\s*\)\s*{[\s\S]*?}", f.read())
    f.close()
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    can_run = True
    for t in tests:
        length = len(re.findall(r"ASSERT", t))
        # config still need more work, file path stuff int(config['run_settings']['max_asserts']):
        # int(config['run_settings']['assert_warning'])
        if length > 20:
            print("ERROR: " + re.findall(r"TEST\s*\(\s*.*\)", t)[0] + " has too many asserts, not running tests!", 'red')
            can_run = False
        elif length > 5:
            print("WARNING: " + re.findall(r"TEST\s*\(\s*.*\)", t)[0] + " has a lot of asserts.")
    return can_run
