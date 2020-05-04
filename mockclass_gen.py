from cpp_gen import CppClass, CppFile
from cpp_parser import CPPParser
import os


def parse_cpp_file(file_obj):
    return CPPParser(file_obj)


def create_mock_class_new(class_name, methods, write_to_disk=True):
    mock_class = MockClass(class_name)
    for m in methods:
        params = [] if not m.params else m.params
        p = []
        for param in params:
            # have to index the first one because param is
            # of the form [type name]
            mock_user_defined_type(param[0])
            if ',' in param:
                p.append("(" + param + ")")
            else:
                p.append(param)
        mock_user_defined_type(m.return_type, write_to_disk=write_to_disk)
        mock_class.add_mock_method(m.return_type, m.name, p,
                                   m.is_virtual, m.is_constant)

        if write_to_disk:
            mock_file = CppFile()
            mock_file.add_component(mock_class.get_class())
            mock_file.write_to_file(mock_class.name)


def create_mock_class_from_file(file_obj, write_to_disk=True):
    # parse file
    parser = CPPParser(file_obj)
    parser.detect_methods()

    # create mock class
    mock_class = MockClass(parser.detected_class_name, inherits=parser.has_virtual_method())
    for m in parser.methods:
        params = [] if not m.params else m.params
        p = []
        for param in params:
            # have to index the first one because param is
            # of the form [type name]
            mock_user_defined_type(param[0])
            if ',' in param:
                p.append("(" + param + ")")
            else:
                p.append(param)
        mock_user_defined_type(m.return_type, write_to_disk=write_to_disk)
        mock_class.add_mock_method(m.return_type, m.name, p,
                                   m.is_virtual, m.is_constant)

    if write_to_disk:
        mock_file = CppFile()
        mock_file.add_component(mock_class.get_class())
        mock_file.write_to_file(mock_class.name)

    return mock_class


def create_mock_class(parser):
    # create mock class
    mock_class = MockClass(parser.detected_class_name, inherits=parser.has_virtual_method())
    for m in parser.methods:
        params = [] if not m.params else m.params
        p = []
        for param in params:
            # have to index the first one because param is
            # of the form [type name]
            mock_user_defined_type(param[0])
            if ',' in param:
                p.append("(" + param + ")")
            else:
                p.append(param)
        mock_user_defined_type(m.return_type)
        mock_class.add_mock_method(m.return_type, m.name, p,
                                   m.is_virtual, m.is_constant)
    return mock_class


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


# finds class in current directory
def find_class_file(class_name):
    if not is_cpp_keyword(class_name):
        if class_file_exists(class_name + ".h"):
            return class_name + ".h"
        elif class_file_exists(class_name + ".cpp"):
            return class_name + ".cpp"
        else:
            for root, dirs, files in os.walk("."):
                for file in files:
                    if file.endswith(".cpp") or file.endswith(".h"):
                        par = CPPParser(open(file))
                        par.ensure_class_detected()
                        if par.detected_class is not None:
                            if par.detected_class_name == class_name:
                                return file
    return None


# if type was already mocked it will do nothing
def mock_user_defined_type(user_type, write_to_disk=True):                  # idk how x::y<w, z> would work
    if not is_cpp_keyword(user_type) and not is_class_mocked(user_type) and "::" not in user_type:
        filename = find_class_file(user_type)
        if filename is not None:
            f = open(filename, 'r')
            create_mock_class_from_file(f, write_to_disk=write_to_disk)


class MockClass:
    def __init__(self, name, inherits=False):
        self.name = "MOCK_" + name
        if inherits:
            self.mock_class = CppClass(self.name, name)
        else:
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
