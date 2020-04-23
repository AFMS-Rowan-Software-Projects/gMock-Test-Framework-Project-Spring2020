#! /usr/bin/python3

import glob, os, pathlib

def find():
    path = pathlib.Path(__file__).parent.absolute()
    os.path.dirname(path)
    for file in glob.glob("MOCK*.*"):
        print(file)
