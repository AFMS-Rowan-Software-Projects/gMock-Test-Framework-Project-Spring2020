import re

# Regex expressions
CLASS_EXP = r'class\s+\S+\s*{[\s\S]*?\n};?'
CLASS_NAME_EXP = r'class \w+'
METHOD_HEADER_EXP = r'((virtual\s)*(const\s)*)*(\w+\s[\w:]+\([\w\s,]*\)\s*)(const\s*)*({|;)'
METHOD_NAME_EXP = r'[\w:]+\('
METHOD_ARGS_EXP = r'\([\w\s,]+\)'

KEYWORDS = ['const', 'virtual']


class CPPParser:
    def __init__(self, cpp_file):
        self.cpp_file = cpp_file
        self.detected_class = None
        self.detected_class_name = None
        self.detected_method_headers = None
        self.methods = []

    def _parse_class(self):
        result = re.findall(CLASS_EXP, self.cpp_file.read())
        if result:
            self.detected_class = result[0]
            self.detected_class_name = self._detect_class_name(self.detected_class)
        else:
            raise ValueError('No class detected in file')

        return result

    def _detect_class_name(self, detected_class):
        class_header = re.findall(CLASS_NAME_EXP, detected_class)[0]
        return class_header.strip().split(" ")[-1]

    def _parse_method_headers(self):

        matches = re.findall(METHOD_HEADER_EXP, self.detected_class)
        result = [''.join(r).strip() for r in matches]
        self.detected_method_headers = result
        return result

    def _parse_return_type(self, header):
        for word in header.split(' '):
            if word not in KEYWORDS:
                return word

    def _parse_is_virtual(self, header):
        return 'virtual' in header.split(' ')

    def _parse_is_const(self, header):
        return 'const' in header.split(' ')

    def _parse_method_name(self, header):
        return re.findall(METHOD_NAME_EXP, header)[0][:-1]

    def _parse_method_args(self, header):
        match = re.findall(METHOD_ARGS_EXP, header)
        if match:
            result = [i.strip().split(' ') for i in match[0][1:-1].split(',')]
        else:
            result = None

        return result

    def detect_methods(self):

        if self.detected_class is None:
            self._parse_class()
        if self.detected_method_headers is None:
            self._parse_method_headers()

        for header in self.detected_method_headers:
            method = DetectedMethod(
                return_type=self._parse_return_type(header),
                name=self._parse_method_name(header),
                is_virtual=self._parse_is_virtual(header),
                is_constant=self._parse_is_const(header),
                params=self._parse_method_args(header)
            )
            self.methods.append(method)

        return self.methods

    def print_detected_methods(self):
        # should say something special if no methods were detected
        for method in self.methods:
            print('Info for method {}:'.format(method.name))
            print('Return type: {}'.format(method.return_type))
            print('Is virtual: {}'.format(method.is_virtual))
            print('Is constant: {}'.format(method.is_constant))
            print('Parameters: {}'.format(method.params))
            print('')


class DetectedMethod:
    def __init__(self, return_type, name, is_virtual, is_constant, params):
        self.return_type = return_type
        self.name = name
        self.is_virtual = is_virtual
        self.is_constant = is_constant
        self.params = params
