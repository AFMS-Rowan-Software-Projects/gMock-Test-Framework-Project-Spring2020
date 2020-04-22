from cpp_gen import CppClass, CppFile
from cpp_parser import CPPParser
import os


def create_mock_class_from_file(file_obj):
    # format file

    # parse file
    parser = CPPParser(file_obj)
    parser.detect_methods()

    # create mock class
    mock_class = create_mock_class(parser)

    # write mock class to file
    mock_file = CppFile()
    mock_file.add_component(mock_class.get_class())
    mock_file.write_to_file(mock_class.name)


def is_cpp_keyword(word):
    keywords = ['bool', 'char', 'char16_t', 'char32_t', 'double', 'float',
                'int', 'long', 'short', 'signed', 'unsigned',
                'void', 'wchar_t']
    return word in keywords


# checks to see if mock file exists (assumes naming convention)
def is_class_mocked(name):
    return class_file_exists(name)


def class_file_exists(name, path="."):
    return name in os.listdir(path)


# if type was already mocked it will do nothing
def mock_user_defined_type(user_type):
    if not is_cpp_keyword(user_type) and not is_class_mocked(user_type):
        print('ATTEMPTING TO CREATE FILENAME')
        print('type: {}, value: {}'.format(type(user_type), user_type))
        filename = user_type + ".cpp"
        if class_file_exists(filename):
            create_mock_class_from_file(filename)


def create_mock_class(parser):
    # create mock class
    mock_class = MockClass(parser.detected_class_name)
    for m in parser.methods:
        params = [] if not m.params else m.params
        for param in params:
            mock_user_defined_type(param)
        mock_user_defined_type(m.return_type)
        mock_class.add_mock_method(m.return_type, m.name, params,
                                   m.is_virtual, m.is_constant)
    return mock_class


class MockClass:
    def __init__(self, name):
        self.name = "MOCK_" + name
        self.mock_class = CppClass(self.name)
        self.mock_class.add_public_specifier()

    # return_type and name are strings, params is a list of strings, virtual and const are booleans
    def add_mock_method(self, return_type, name, params, virtual, const):
        statement = "MOCK_METHOD(" + return_type + ", " + name + ", ("
        params_as_list_of_str = [' '.join(i) for i in params]
        statement += ', '.join(params_as_list_of_str)
        statement = statement + ")"

        if virtual:
            statement = statement + ", (override"
            if const:
                statement = statement + ", const))"
            else:
                statement = statement + "))"
        else:
            if const:
                statement = statement + ", (const))"
            else:
                statement = statement + ")"

        self.mock_class.add_statement(statement, indent=True,
                                      has_semicolon=True)

    def get_class(self):
        return self.mock_class