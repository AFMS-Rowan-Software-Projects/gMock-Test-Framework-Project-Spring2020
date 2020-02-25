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

    def generate(self):
        result = ''
        result += ''.join(self.includes)
        result += ''.join(self.namespaces)
        result += ''.join(self.methods)

        return result


class Method:
    def __init__(self, return_type, name):
        self.return_type = return_type
        self.name = name
        self.return_statement = ''
        self.statements = []
        self.locals = {}

    def generate_statements(self):
        return ''.join([*self.statements, self.return_statement])

    def add_locals(self, type, name, init_value):
        # self.locals[]
        pass

    def add_cout(self, value):
        value = '"{}"'.format(value).replace("\n", "\\n")
        self.statements.append('\tcout << {};\n'.format(value))

    def add_return(self, value):
        self.return_statement = '\treturn {};\n'.format(value)

    def generate(self):
        return "{} {}()\n{{\n{}\n}}".format(self.return_type,
                                                self.name,
                                                self.generate_statements())


