import subprocess, platform, re, configparser, time

totalRegex = re.compile(r'\[==========\] Running [0-9]+ test')
passedRegex = re.compile(r'\[  PASSED  \] [0-9]+ test')
numRegex = re.compile(r'[0-9]+')


def run_tests(filename, testname=None, subtestname=None):
    sys = platform.system()
    temp = filename
    will_run = True
    command = []
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
            command.append("./{}".format(temp))
            if testname is not None:
                if subtestname is None:
                    command.append("--gtest_filter={}.*".format(testname))
                else:
                    command.append("--gtest_filter={}.{}*".format(testname, subtestname))

            process = run_with_max_time(command, 5)
            if process is None:
                print("Tests ran for longer than the maximum allotted time!")
            else:
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


# command should be an array of arguements,
# like ["./{}".format(temp), "--gtest_filter={}.{}*".format(testname, subtestname)]
def run_with_max_time(command, timeout):
    p = subprocess.Popen(command, shell=False)

    while timeout > 0:
        print(timeout)
        if p.poll() is not None:
            return subprocess.check_output(command)
        time.sleep(0.1)
        timeout -= 0.1
    else:
        try:
            p.kill()
        except OSError as e:
            if e.errno != 3:
                raise
    return None
