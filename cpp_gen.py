class CppFile:
    def __init__(self):
        self.includes = []
        self.namespaces = []
        self.methods = []

    def add_include(self, include):
        self.includes.append('#include <{}>\n'.format(include))

    def add_namespace(self, namespace):
        self.namespaces.append('using namespace {};\n'.format(namespace))

    def add_method(self, method):
        self.methods.append(method.generate())

    def add_macro_function(self, macro_func):
        self.methods.append(macro_func.generate())

    def generate(self):
        result = ''
        result += ''.join(self.includes)
        result += ''.join(self.namespaces)
        result += ''.join(self.methods)

        return result


class Method:
    def __init__(self, return_type, name, *args):
        self.return_type = return_type
        self.name = name
        self.args = args
        self.return_statement = ''
        self.statements = []

    def add_cout(self, value):
        value = '"{}"'.format(value).replace("\n", "\\n")
        self.statements.append('\tcout << {} << endl;\n'.format(value))

    def add_return(self, value):
        self.return_statement = '\treturn {};\n'.format(value)

    def add_method_call(self, name, *args):
        self.statements.append('\t{}({});\n'.format(name,
                                                    self._convert_args_to_str(
                                                        args)))

    def generate(self):
        return "{} {}({})\n{{\n{}\n}}\n\n".format(self.return_type,
                                                  self.name,
                                                  self._convert_args_to_str(
                                                      self.args),
                                                  self._generate_statements())

    def _convert_args_to_str(self, args):
        return ','.join(str(x) for x in args)

    def _generate_statements(self):
        return ''.join([*self.statements, self.return_statement])


class MacroFunction:
    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.statements = []

    def add_cout(self, value):
        value = '"{}"'.format(value).replace("\n", "\\n")
        self.statements.append('\tcout << {} << endl;\n'.format(value))

    def add_macro_call(self, name, *args):
        self.statements.append('\t{}({});\n'.format(name,
                                                    self._convert_args_to_str(
                                                        args)))

    def generate(self):
        return "{}({})\n{{\n{}\n}}\n\n".format(self.name,
                                               self._convert_args_to_str(
                                                   self.args),
                                               self._generate_statements())

    def _convert_args_to_str(self, args):
        return ','.join(str(x) for x in args)

    def _generate_statements(self):
        return ''.join(self.statements)
