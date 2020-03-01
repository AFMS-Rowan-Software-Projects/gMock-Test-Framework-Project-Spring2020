from cpp_gen import CppFile, CppClass

class MockClass:
    def __init__(self, name):
        self.cpp = CppFile()
        self.mock_class = CppClass("MOCK" + name)
        self.mock_class.add_public_specifier()

    # return_type and name are strings, params is a list of strings, virtual and const are booleans
    def add_mock_method(self, return_type, name, params, virtual, const):
        statement = "MOCK_METHOD(" + return_type + ", " + name + ", ("
        length = len(params)
        for i in range(length-1):
            statement = statement + params[i] + ", "
        if length > 0:
            statement = statement + params[length - 1]
        statement = statement + ")"
        if virtual:
            statement = statement + ", (override"
            if const:
                statement = statement + ", const))"
            else:
                statement = statement + "))"
        else:
            if const:
                statement = statement + "(const))"
            else:
                statement = statement + ")"

        self.mock_class.add_statement(statement, indent=True, has_semicolon=True)

    def generate(self):
        self.cpp.add_component(self.mock_class)
        return self.cpp.generate()