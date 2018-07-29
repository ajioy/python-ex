# -*- coding:utf-8 -*-
class Animal(object):
  pass

class Mammal(Animal):
  pass

class Bird(Animal):
  pass

class Dog(Mammal):
  pass

class Bat(Mammal):
  pass

class Parrot(Bird):
  pass

class Ostrich(Bird):
  pass

class RunnableMixin(object):
  def run(self):
    print('Running...')

class FlyableMixin(object):
  def fly(self):
    print('Flying...')

class Dog(Mammal, RunnableMixin):
  pass

class Bat(Mammal, FlyableMixin):
  pass

d = Dog()
d.run()
b = Bat()
b.fly()

class MyTCPServer(TCPServer, ForkingMixin):
  pass

class MyUDPServer(UDPServer, ThreadingMixin):
  pass

class MyTCPServerEx(TCPServer, CoroutineMixin):
  pass

