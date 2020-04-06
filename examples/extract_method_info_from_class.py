from cpp_parser import CPPParser

file_path = r'geeks.cpp'
file = open(file_path, 'r')
parser = CPPParser(file)
parser.detect_methods()

print('Detected {} methods in the class\n'.format(len(parser.methods)))

for m in parser.methods:
    print('Info for method {}:'.format(m.name))
    print('Return type: {}'.format(m.return_type))
    print('Is virtual: {}'.format(m.is_virtual))
    print('Is constant: {}'.format(m.is_constant))
    print('Parameters: {}'.format(m.params))
    print('')

# Output:

# Detected 2 methods in the class
#
# Info for method printName:
# Return type: void
# Is virtual: False
# Is constant: True
# Parameters: None
#
# Info for method doNothing:
# Return type: int
# Is virtual: False
# Is constant: False
# Parameters: [['int', 'arg1'], ['double', 'arg2']]
