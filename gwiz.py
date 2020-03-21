import sys
from cpp_gen import CppFile
from cpp_parser import *
import config_modifier
from format_cpp_file import format_file
import os
from mockclass_gen import create_mock_class_from_file

from cpp_parser import CPPParser

#save the file argument to a variable
filename = sys.argv[1]

fp = open(filename)

mock_class_file = create_mock_class_from_file(fp)
