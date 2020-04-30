# This file contains classes that are used to generate C++ files

class CppFile:
    def __init__(self):
        self.includes = []
        self.namespaces = []
        self.components = []

    # include other file that this class is dependent on
    def add_include(self, include):
        # if/else checks if the include already ends with <> or ""
        if include.endswith(">") or include.endswith("\""):
            self.includes.append('#include {}\n'.format(include))
        else:
            self.includes.append('#include <{}>\n'.format(include))

    # specify which namespace to use
    def add_namespace(self, namespace):
        self.namespaces.append('using namespace {};\n'.format(namespace))

    # A component is a Python class with a generate method. When the CppFile
    # is generated the .generate() method will be called on each component added
    # to CppFile.
    def add_component(self, component):
        if 'generate' not in dir(component):
            msg = '{} does not have attribute generate'.format(component)
            raise TypeError(msg)

        self.components.append(component.generate())

    # Assembles a string representing the contents of the CppFile
    def generate(self):
        result = ''
        result += ''.join(self.includes) + '\n\n'
        result += ''.join(self.namespaces) + '\n'
        result += ''.join(self.components)

        return result

    # Write the assembled string to file
    def write_to_file(self, filename):
        filename = '{}.cpp'.format(filename.split('.')[0])
        with open(filename, 'w') as file:
            file.write(self.generate())


# static methods
def convert_params_to_str(params, sep=', '):
    return '{}'.format(sep).join(str(x) for x in params)


class StatementGroup:
    # Represents a group of C++ statements

    def __init__(self):
        self.statements = []
        self.statements_before_specifiers = None
        self.public_specifier = None
        self.private_specifier = None

    # Append a statement to the group
    def add_statement(self, expression, indent=True, has_semicolon=True):
        indent = '\t' if indent else ''
        semicolon = ';' if has_semicolon else ''
        self.statements.append(
            '{}{}{}\n'.format(indent, expression, semicolon))

    # If statements were added before an access specifier (public/private), this
    # must be called. It will save those statements so that they can be written outside
    # the public/private groups. For example:
    #
    #     class Rectangle {
    #         int width, height;    -----> This statement is before the public block
    #       public:
    #         void set_values(int,int) {
    #             width = x;
    #             height = y;
    #         }
    #         int area() {return width*height;}
    #     };
    #
    # In order to save the statement 'int width, height;' this method
    # would have to be called before add_public_specifier().
    def preserve_statements_before_specifiers(self):
        if self.statements_before_specifiers is None:
            self.statements_before_specifiers = self.statements
            self.statements = []

    # Add public block. All further statements added to the StatementGroup will
    # go inside this public block (until another block is added)
    def add_public_specifier(self):
        self.preserve_statements_before_specifiers()
        self.public_specifier = StatementGroup()
        self.public_specifier.add_statement('public:', indent=False,
                                            has_semicolon=False)
        return self.public_specifier

    # Add private block. All further statements added to the StatementGroup will
    # go inside this public block (until another block is added)
    def add_private_specifier(self):
        self.preserve_statements_before_specifiers()
        self.private_specifier = StatementGroup()
        self.private_specifier.add_statement('private:', indent=False,
                                             has_semicolon=False)
        return self.private_specifier

    # Adds a blank line
    def add_white_space(self, amount=1):
        for i in range(amount):
            self.add_statement("", has_semicolon=False)

    # Add comment
    def add_comment(self, comment):
        slashes_with_comment = '// ' + comment
        self.add_statement(slashes_with_comment, has_semicolon=False)

    # Add cout statement. Assumes you are using the std namespace.
    def add_cout(self, message):
        msg_with_quotes = '"{}"'.format(message)
        expression = 'cout << {} << endl'.format(msg_with_quotes)
        self.add_statement(expression)

    # Adds a statement that calls a C++ function. The name parameter is
    # the name of the function you want to call.
    def add_function_call(self, name, *params, namespace=None):
        if namespace:
            name = '{}::{}'.format(namespace, name)
        params_as_str = convert_params_to_str(params)
        self.add_statement('{}({})'.format(name, params_as_str))

    # The following methods add statements related to GTest
    def add_assert_true(self, condition='condition'):
        self.add_function_call('ASSERT_TRUE', condition)

    def add_assert_false(self, condition='condition'):
        self.add_function_call('ASSERT_FALSE', condition)

    def add_assert_eq(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('ASSERT_EQ', val_1, val_2)

    def add_assert_ne(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('ASSERT_NE', val_1, val_2)

    def add_assert_lt(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('ASSERT_LT', val_1, val_2)

    def add_assert_le(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('ASSERT_LE', val_1, val_2)

    def add_assert_gt(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('ASSERT_GT', val_1, val_2)

    def add_assert_ge(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('ASSERT_GE', val_1, val_2)

    def add_expect_true(self, condition='condition'):
        self.add_function_call('EXPECT_TRUE', condition)

    def add_expect_false(self, condition='condition'):
        self.add_function_call('EXPECT_FALSE', condition)

    def add_expect_eq(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('EXPECT_EQ', val_1, val_2)

    def add_expect_ne(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('EXPECT_NE', val_1, val_2)

    def add_expect_lt(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('EXPECT_LT', val_1, val_2)

    def add_expect_le(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('EXPECT_LE', val_1, val_2)

    def add_expect_gt(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('EXPECT_GT', val_1, val_2)

    def add_expect_ge(self, val_1='val_1', val_2='val_2'):
        self.add_function_call('EXPECT_GE', val_1, val_2)

    def add_nice_mock(self, class_name='mock_class_name'):
        self.add_statement("NiceMock<" + class_name + "> var_name")

    def add_strict_mock(self, class_name='mock_class_name'):
        self.add_statement("StrictMock<" + class_name + "> var_name")

    # Generates all the different components making up the StatementGroup
    # by converting them to a string
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


# A StatementGroup with braces and an optional semicolon
class CodeBlock(StatementGroup):
    def __init__(self, has_semicolon=False):
        StatementGroup.__init__(self)
        self.has_semicolon = has_semicolon

    # Creates a string representing the CodeBlock
    def generate(self):
        semicolon = ';' if self.has_semicolon else ''
        all_statements = StatementGroup.generate(self)
        return '{{\n{}}}{}\n\n'.format(all_statements, semicolon)


# Represents a C++ Class
class CppClass(CodeBlock):
    def __init__(self, name, base_class=None):
        CodeBlock.__init__(self, has_semicolon=True)
        self.header = self._generate_header(name, base_class)

    # Generates the header for the C++ class
    def _generate_header(self, name, base_class):
        if base_class:
            derivation_list = ' : public {}'.format(base_class)
        else:
            derivation_list = ''

        return 'class {}{} '.format(name, derivation_list)

    # Creates a string generating the C++ class
    def generate(self):
        return self.header + CodeBlock.generate(self)


# Represents a function in a C++ class
class Function(CodeBlock):
    def __init__(self, return_type, name, *params):
        CodeBlock.__init__(self)
        self.header = self._generate_header(return_type, name, *params)

    def _generate_header(self, return_type, name, *params):
        params_as_str = convert_params_to_str(params)
        return '{} {}({}) '.format(return_type, name, params_as_str)

    # Add return statement
    def add_return(self, expression):
        return_and_expr = 'return {}'.format(expression)
        self.add_statement(return_and_expr)

    # Add GTest method that runs all the tests
    def add_run_all_tests_and_return(self):
        self.add_return('RUN_ALL_TESTS()')

    def generate(self):
        return self.header + CodeBlock.generate(self)


# Creates a MacroFunction in the C++ class
# Note: MacroFunctions are handled by the C++ preprocessor
class MacroFunction(CodeBlock):
    def __init__(self, name, *params):
        CodeBlock.__init__(self)
        self.header = self._generate_header(name, *params)

    def _generate_header(self, name, *params):
        params_as_str = convert_params_to_str(params)
        return '{}({}) '.format(name, params_as_str)

    def generate(self):
        return self.header + CodeBlock.generate(self)
