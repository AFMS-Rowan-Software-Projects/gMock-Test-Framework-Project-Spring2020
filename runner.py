import ctypes


_test = ctypes.CDLL('./hello_world.so')

_test.test()
