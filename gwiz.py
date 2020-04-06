import sys
from mockclass_gen import create_mock_class_from_file
from full_file_creator import make_full_file

# save the file argument to a variable
filename = sys.argv[1]

if len(sys.argv) > 2 and sys.argv[2].lower() == "full":
    make_full_file(filename).write_to_file("MOCK_" + filename)
else:
    fp = open(filename)
    mock_class_file = create_mock_class_from_file(fp)
