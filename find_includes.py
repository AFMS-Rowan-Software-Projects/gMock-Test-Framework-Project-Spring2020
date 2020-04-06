import re

def find_every_include(fileName):
    f = open(fileName)
    result = re.findall(r'#include .*>', open(fileName).read())
    f.close()
    return result
