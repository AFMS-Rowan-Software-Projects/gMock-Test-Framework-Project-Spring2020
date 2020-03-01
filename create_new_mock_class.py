from mockclass_gen import MockClass
from cpp_gen import CppFile


def new_mock_class_manual():
    name = input("Enter the name of the class: ")

    mc = MockClass(name)

    num_methods = int(input("Enter the amount of methods the class has: "))

    for i in range(num_methods):
        mname = input("Enter the name of method " + str(i) + ": ")
        rt = input("Enter the return type of method " + mname + ": ")

        v = input("Is the method virtual? (Y/N): ")
        if v.lower() == "y":
            virt = True
        else:
            virt = False

        c = input("Is the method const? (Y/N): ")
        if c.lower() == "y":
            con = True
        else:
            con = False

        num_params = int(input("Enter the number of parameters for the method: "))
        params = []
        for j in range(num_params):
            params.append(input("Enter parameter " + str(j) + ": "))
        mc.add_mock_method(rt, mname, params, virtual=virt, const=con)

    return mc


cpp = CppFile()
cpp.add_component(new_mock_class_manual().get_class())
print(cpp.generate())