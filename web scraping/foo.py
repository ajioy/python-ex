#coding:utf-8
class Ajioy:
    def __init__(self):
        self.name = 'ajioy'
        self.age = 26
        self.sex = 'male'
        self.height = 170

    def getName(self):
        return self.name

    def setHeight(self, myAge):
        self.age = myAge

    def __private(self):
        print "you can't see me!"


cls = Ajioy()
print cls.getName()

cls.setHeight(28)
print cls.age

#cls.__private()
