from cpp_gen import CppFile, CppClass

cpp = CppFile()

# create class
my_class = CppClass('MyClass')
my_class_public = my_class.add_public_specifier()
my_class_public.add_comment('You could put constructors here')
my_class_public.add_comment('You could put public methods here')
my_class_private = my_class.add_private_specifier()
my_class_private.add_comment('You could put private methods here')

# add methods
cpp.add_component(my_class)
print(cpp.generate())

# output (note this does not compile):

# class MyClass {
# public:
# 	// You could put constructors here
# 	// You could put public methods here
# private:
# 	// You could put private methods here
# };

