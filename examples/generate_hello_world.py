from cpp_gen import CppFile, Method


f = CppFile()

# add includes
f.add_include('iostream')
f.add_namespace('std')

# main method definition
main_method = Method('int', 'main')
main_method.add_cout('Hello World1!')
main_method.add_cout('Hello World2!')
main_method.add_cout('Hello World3!')
main_method.add_return(0)

# add methods
f.add_method(main_method)
print(f.generate())
