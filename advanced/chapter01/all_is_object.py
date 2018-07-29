def ask(name="ajioy1"):
    print(name)

class Person:
    def __init__(self):
        print("ajioy2")

obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())

def decorator_func():
    print("dec start")
    return ask

my_ask = decorator_func()
my_ask("Jim")
#my_func = ask
#my_func("ajioy scotte")
#
#my_class = Person
#my_class()