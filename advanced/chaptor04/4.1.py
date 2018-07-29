class Cat(object):
    def say(self):
        print("I am a cat")

class Dog(object):
    def say(self):
        print("I am a dog")

class Duck(object):
    def say(self):
        print("I am a duck")

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


# c++/java用以下方式实现
class Animal:
    def say(self):
        print("I am a animal")

class Cat(Animal):
    def say(self):
        print("I am a cat")

cat = Cat()
cat.say()

a = ["ajioy1", "ajioy2"]
b = ["ajioy2", "ajioy"]
name_tuple = ["ajioy3", "ajioy4"]
name_set = set()
name_set.add("ajioy5")
name_set.add("ajioy6")
# 只要是可迭代类型都可以使用
# 鸭子类型
#a.extend(b)
#a.extend(name_tuple)
a.extend(name_set)
print(a)
