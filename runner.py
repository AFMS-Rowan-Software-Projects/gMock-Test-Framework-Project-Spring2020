import subprocess


print("hello")

process = subprocess.call('hello_world', shell=False)

print(process)
