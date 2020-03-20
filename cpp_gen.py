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


class StatementGroup:
    def __init__(self):
        self.statements = []
        self.statements_before_specifiers = None
        self.public_specifier = None
        self.private_specifier = None

    def add_statement(self, expression, indent=True, has_semicolon=True):
        indent = '\t' if indent else ''
        semicolon = ';' if has_semicolon else ''
        self.statements.append(
            '{}{}{}\n'.format(indent, expression, semicolon))

    def preserve_statements_before_specifiers(self):
        if self.statements_before_specifiers is None:
            self.statements_before_specifiers = self.statements
            self.statements = []

    def add_public_specifier(self):
        self.preserve_statements_before_specifiers()
        self.public_specifier = StatementGroup()
        self.public_specifier.add_statement('public:', indent=False,
                                            has_semicolon=False)
        return self.public_specifier

    def add_private_specifier(self):
        self.preserve_statements_before_specifiers()
        self.private_specifier = StatementGroup()
        self.private_specifier.add_statement('private:', indent=False,
                                             has_semicolon=False)
        return self.private_specifier

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

    def add_nice_mock(self):
        self.add_statement('NiceMock<mock_class_name> var_name')
    def add_nice_mock(self, class_name):
        self.add_statement("NiceMock<" + class_name + "> var_name")

    def add_strict_mock(self):
        self.add_statement('StrictMock<mock_class_name> var_name')
    def add_strict_mock(self, class_name):
        self.add_statement("StrictMock<" + class_name + "> var_name")

    def generate(self):
        if self.statements_before_specifiers:
            # do not change self.statements_before_specifiers incase
            # the generate() method is called more than once
            before_statements = self.statements_before_specifiers
        else:
            before_statements = ['']

        if self.public_specifier:
            public_statements = self.public_specifier.generate()
        else:
            public_statements = ['']

        if self.private_specifier:
            private_statements = self.private_specifier.generate()
        else:
            private_statements = ['']

        return ''.join(
            [*before_statements, *public_statements, *private_statements,
             *self.statements])


class CodeBlock(StatementGroup):
    def __init__(self, has_semicolon=False):
        StatementGroup.__init__(self)
        self.has_semicolon = has_semicolon

    def generate(self):
        semicolon = ';' if self.has_semicolon else ''
        all_statements = StatementGroup.generate(self)
        return '{{\n{}}}{}\n\n'.format(all_statements, semicolon)


class CppClass(CodeBlock):
    def __init__(self, name, base_class=None):
        CodeBlock.__init__(self, has_semicolon=True)
        self.header = self._generate_header(name, base_class)

    def _generate_header(self, name, base_class):
        if base_class:
            derivation_list = ' : public {}'.format(base_class)
        else:
            derivation_list = ''

        return 'class {}{} '.format(name, derivation_list)

    def generate(self):
        return self.header + CodeBlock.generate(self)


class Function(CodeBlock):
    def __init__(self, return_type, name, *params):
        CodeBlock.__init__(self)
        self.header = self._generate_header(return_type, name, *params)

    def _generate_header(self, return_type, name, *params):
        params_as_str = convert_params_to_str(params)
        return '{} {}({}) '.format(return_type, name, params_as_str)

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
        return '{}({}) '.format(name, params_as_str)

    def generate(self):
        return self.header + CodeBlock.generate(self)
