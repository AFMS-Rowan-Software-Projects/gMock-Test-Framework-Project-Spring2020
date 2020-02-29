from cpp_gen import CppFile, Function

func_1 = Function('int', 'main')
func_1.add_comment('this is a comment')
func_1.add_cout('Hello world!')

cpp = CppFile()
cpp.add_include('iostream')
cpp.add_namespace('std')
cpp.add_component(func_1)
cpp.write_to_file('hello_world')

