from cpp_parser import CPPParser

fileobj = open('geeks.cpp')
parser = CPPParser(fileobj)
parser.detect_public_methods()
parser.print_detected_method_info(parser.public_methods)


