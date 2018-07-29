def my_abs(x):
  if x >= 0:
    return x
  else:
    return -x


print(my_abs(-123))
print(my_abs(123))

def nop():
  pass

print(nop())

print(my_abs('A'))
# print(abs('A'))
def my_abs(x):
  if not isinstance(x, (int, float)):
    raise TypeError('bad operand type')
  if x >= 0:
    return x
  else:
    return -x

print(my_abs(11231))
print(my_abs(-231))
# print(my_abs('a'))

def power(x, n=2):
  s = 1
  while n > 0:
    n = n - 1
    s = s * x
  return s

print power(2,4)


def add_end(L = None):
  if L is None:
    L = []
  L.append('END')
  return L

print(add_end())
print(add_end())

def calc(numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum

print calc([1,2,3])
print calc((1,2,3,4))

def calc2(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum

print calc2(1,2,3,4)
numbers = (1,2,3)
print(calc2(*numbers))


def person(name, age, **kw):
  print 'name:', name, 'age:', age, 'other:', kw

print(person('Ajioy',28))
print(person('Ajioy',28,city='Wuhan'))
print(person('Ajioy',28,city='Wuhan', height=1.81))

def func(a, b, c=0, *args, **kw):
  print 'a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw

func(1,2)
func(1,2,10)
func(1,2,10,'a', 'b')
func(1,2,10,'a', 'b', city='wuhan', m='male')
# func(1,2,10,'a', city='wuhan','b' , m='male')

def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n - 1)

print fact(5)
print fact(100)
#print fact(1000)

def fact2(n):
  return fact_iter(n, 1)

def fact_iter(num, product):
  if num == 1:
    return product
  else:
    return fact_iter(num - 1, num * product)

print fact2(5)
print fact2(10)
print fact2(100)
# print fact2(1000)
