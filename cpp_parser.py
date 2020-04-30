import re

# Regex expressions
CLASS_EXP = r'class\s+\S+\s*(?::*\s+(?:public|protected|private)\s+\S+\s*,*)*{[\s\S]*?\n};?'
CLASS_INHERITANCE = r'(?:public|protected|private)\s+\w+'
CLASS_NAME_EXP = r'class \w+'
METHOD_HEADER_EXP = r'((virtual\s)*(const\s)*)*((?:unsigned )?\w+\s[\w:]+\s*\([\w\s,*&]*\)\s*)(const\s*)*({|.*?;)'
METHOD_NAME_EXP = r'[\w:]+\('
METHOD_ARGS_EXP = r'\([\w\s,*&]+\)'
PUBLIC_BLOCK_EXP = r'public\s*:.*?[\s\S]*?(?:private\s*:|protected\s*:|};)'
PROTECTED_BLOCK_EXP = r'protected\s*:.*?[\s\S]*?(?:private\s*:|public\s*:|};)'

KEYWORDS = ['const', 'virtual']


# Given a path to a cpp file this class will provide tools to extract
# information from the class
class CPPParser:
    def __init__(self, cpp_file):
        self.cpp_file = cpp_file
        self.detected_class = None
        self.detected_class_name = None
        self.detected_method_headers = None
        self.methods = []
        self.public_methods = []
        self.protected_methods = []
        self.superclasses = []
        self.includes = []

    # finds the class in the file
    def _parse_class(self):
        file_text = self.cpp_file.read()
        self.includes = re.findall(r'#include .*[">]\n', file_text)
        result = re.findall(CLASS_EXP, file_text)
        if result:
            self.detected_class = result[0]
            self.detected_class_name = self._detect_class_name(
                self.detected_class)
        # else:
        #    raise ValueError('No class detected in file')

        return result

    # extracts the class name from a class
    def _detect_class_name(self, detected_class):
        class_header = re.findall(CLASS_NAME_EXP, detected_class)[0]
        return class_header.strip().split(" ")[-1]

    # parses method headers from block of code
    def _parse_method_headers(self, block):
        matches = re.findall(METHOD_HEADER_EXP, block)
        result = [''.join(r).strip() for r in matches]
        self.detected_method_headers = result
        return result

    # detects the return type of a method header
    def _parse_return_type(self, header):
        temp = header.split()
        for wordnum in range(0, len(temp)):
            word = temp[wordnum]
            if word not in KEYWORDS:
                if word == "unsigned":
                    return word + " " + temp[wordnum + 1]
                else:
                    return word

    # determines if the method is virtual of a method header
    def _parse_is_virtual(self, header):
        return 'virtual' in header.split(' ')

    # determines if the method is const of a method header
    def _parse_is_const(self, header):
        return 'const' in header.split(' ')

    # determines the method name from a method header
    def _parse_method_name(self, header):
        return re.findall(METHOD_NAME_EXP, header)[0][:-1]

    # determines the method args from a method header
    def _parse_method_args(self, header):
        match = re.findall(METHOD_ARGS_EXP, header)
        if match:
            result = [i.strip().split(' ') for i in match[0][1:-1].split(',')]
        else:
            result = None

        return result

    # parses public block from block of code
    def _parse_public_block(self, block):
        matches = re.findall(PUBLIC_BLOCK_EXP, block)
        result = [''.join(r).strip() for r in matches]
        self.detected_method_headers = result
        return result

    # parses protected block from block of code
    def _parse_protected_block(self, block):
        matches = re.findall(PROTECTED_BLOCK_EXP, block)
        result = [''.join(r).strip() for r in matches]
        self.detected_method_headers = result
        return result

    # checks to see if there is a class detected
    def ensure_class_detected(self):
        if self.detected_class is None:
            self._parse_class()

    # converts method headers to a DetectedMethod object
    def _convert_headers_to_detect_methods(self, headers):
        result = []
        for header in headers:
            result.append(DetectedMethod(
                return_type=self._parse_return_type(header),
                name=self._parse_method_name(header),
                is_virtual=self._parse_is_virtual(header),
                is_constant=self._parse_is_const(header),
                params=self._parse_method_args(header)
            ))

        return result

    # detects methods from class
    def detect_methods(self):
        self.ensure_class_detected()
        self._parse_method_headers(self.detected_class)
        self.methods.extend(self._convert_headers_to_detect_methods(
            self.detected_method_headers))

        return self.methods

    # Print out the info for detect methods class
    def print_detected_method_info(self, methods):
        if not methods:
            print('No methods were given')
        else:
            for method in methods:
                # probably should loop through attributes instead of hard coding
                print('Info for method {}:'.format(method.name))
                print('Return type: {}'.format(method.return_type))
                print('Is virtual: {}'.format(method.is_virtual))
                print('Is constant: {}'.format(method.is_constant))
                print('Parameters: {}'.format(method.params))
                print('')

    # detects public methods from class
    def detect_public_methods(self):
        self.ensure_class_detected()
        result = re.findall(PUBLIC_BLOCK_EXP, self.detected_class)
        if result:
            public_block = result[0]
            headers = self._parse_method_headers(public_block)
            self.public_methods = self._convert_headers_to_detect_methods(headers)

    # detects protected methods from class
    def detect_protected_methods(self):
        self.ensure_class_detected()
        result = re.findall(PROTECTED_BLOCK_EXP, self.detected_class)
        if result:
            protected_block = result[0]
            headers = self._parse_method_headers(protected_block)
            self.protected_methods = self._convert_headers_to_detect_methods(headers)

    # detects superclasses in the current class
    def detect_superclasses(self):
        scs = re.findall(CLASS_INHERITANCE, self.detected_class)
        for c in scs:
            self.superclasses.append(c.split(" "[1]))

    def has_virtual_method(self):
        for m in self.methods:
            if m.is_virtual:
                return True
        return False

    # RETURNS THE BASE CLASS AS TEXT
    def generate(self):
        return self.detected_class + '\n\n'


# a class that holds information about a method in its state
class DetectedMethod:
    def __init__(self, return_type, name, is_virtual, is_constant, params):
        self.return_type = return_type
        self.name = name
        self.is_virtual = is_virtual
        self.is_constant = is_constant
        self.params = params
