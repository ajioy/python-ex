a = 1 # a是int类生成的对象
b = "hello"
print(type(1)) # int->1
print(type(b)) # str->"hello"
print(type(int)) # type->int
print(type(str)) # type->str

class Student:
    pass

stu = Student()
print(type(stu))
print(Student.__bases__)

class MyStudent(Student):
    pass

print(MyStudent.__bases__) # class 'Student'
print(type.__bases__) # object
print(type(object)) # none
print(object.__bases) # type