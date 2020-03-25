import sys
from mockclass_gen import create_mock_class_from_file

# save the file argument to a variable
filename = sys.argv[1]

fp = open(filename)

mock_class_file = create_mock_class_from_file(fp)
