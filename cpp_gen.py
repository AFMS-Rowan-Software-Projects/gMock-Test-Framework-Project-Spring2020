class CppFile:
    def __init__(self):
        self.includes = []
        self.namespaces = []
        self.components = []

    def add_include(self, include):
        self.includes.append('#include <{}>\n'.format(include))

    def add_namespace(self, namespace):
        self.namespaces.append('using namespace {};\n'.format(namespace))

    def add_component(self, component):
        if 'generate' not in dir(component):
            msg = '{} does not have attribute generate'.format(component)
            raise TypeError(msg)

        self.components.append(component.generate())

    def generate(self):
        result = ''
        result += ''.join(self.includes) + '\n'
        result += ''.join(self.namespaces) + '\n'
        result += ''.join(self.components)

        return result

    def write_to_file(self, filename):
        filename = '{}.cpp'.format(filename.split('.')[0])
        with open(filename, 'w') as file:
            file.write(self.generate())


# static methods
def convert_params_to_str(params, sep=', '):
    return '{}'.format(sep).join(str(x) for x in params)


class CodeBlock:
    def __init__(self):
        self.statements = []

    def add_statement(self, expression, has_semicolon=True):
        semicolon = ';' if has_semicolon else ''
        self.statements.append('\t{}{}\n'.format(expression, semicolon))

    def add_comment(self, comment):
        slashes_with_comment = '// ' + comment
        self.add_statement(slashes_with_comment, has_semicolon=False)

    def add_cout(self, message):
        msg_with_quotes = '"{}"'.format(message)
        expression = 'cout << {} << endl'.format(msg_with_quotes)
        self.add_statement(expression)

    def add_function_call(self, name, *params, namespace=None):
        if namespace:
            name = '{}::{}'.format(namespace, name)
        params_as_str = convert_params_to_str(params)
        self.add_statement('{}({})'.format(name, params_as_str))

    def add_assert_eq(self, val_1, val_2):
        self.add_function_call('ASSERT_EQ', val_1, val_2)

    def generate(self):
        all_statements = ''.join(self.statements)
        return '{{\n{}}}\n\n'.format(all_statements)


class Function(CodeBlock):
    def __init__(self, return_type, name, *params):
        CodeBlock.__init__(self)
        self.header = self._generate_header(return_type, name, *params)

    def _generate_header(self, return_type, name, *params):
        params_as_str = convert_params_to_str(params)
        return '{} {}({})'.format(return_type, name, params_as_str)

    def add_return(self, expression):
        return_and_expr = 'return {}'.format(expression)
        self.add_statement(return_and_expr)

    def add_run_all_tests_and_return(self):
        self.add_return('RUN_ALL_TESTS()')

    def generate(self):
        return self.header + CodeBlock.generate(self)


class MacroFunction(CodeBlock):
    def __init__(self, name, *params):
        CodeBlock.__init__(self)
        self.header = self._generate_header(name, *params)

    def _generate_header(self, name, *params):
        params_as_str = convert_params_to_str(params)
        return '{}({})'.format(name, params_as_str)

    def generate(self):
        return self.header + CodeBlock.generate(self)
