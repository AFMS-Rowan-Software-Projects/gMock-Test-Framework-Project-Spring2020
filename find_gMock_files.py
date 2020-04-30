#! /usr/bin/python3

import glob, os, pathlib

# Goes through directory and finds all mock classes
def find():
    path = pathlib.Path(__file__).parent.absolute()
    os.path.dirname(path)
    for file in glob.glob("MOCK*.*"):
        print(file)
