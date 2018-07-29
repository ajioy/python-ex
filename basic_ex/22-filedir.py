#!/usr/bin/env python
#-*- coding: utf-8 -*-


try:
  f = open('./hello.py', 'r')
  print f.read()
except:
  print "error occur!"
finally:
  if f:
    f.close()

with open('./hello.py', 'r') as f:
  print f.read()

# read config 
# for line in f.readlines():
#   print(line.strip())
# with open('./test.jpg', 'rb') as f:
#   print f.read()

f = open('./write.txt', 'w')
f.write('hello, ajioy!\n')
f.write('I am a goodboy...')
f.close()


print '*' * 20

import os
print os.name # 'nt':windows 'posix':linux, mac...

#print os.environ
print os.getenv('PATH')

print '*' * 20
print os.path.abspath('.')
path = os.path.abspath('.')
new_path = os.path.join(path, 'testdir')
print new_path
os.mkdir(new_path)
os.rmdir(new_path)

new_path = os.path.join(new_path, 'test.txt')
print new_path
print os.path.split(new_path)
print os.path.splitext(new_path)

#os.rename('hello.txt', 'hello.py')
os.remove('write.txt')

print os.listdir('.')
print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and
    os.path.splitext(x)[1] == '.py']

with open('./all.txt', 'w') as f:
  #maps = map(lambda x: x+'\n', all_list)
  maps = [x+'\n' for x in os.listdir('.') if os.path.isfile(x) and
      os.path.splitext(x)[1] == '.py']
  for s in maps:
    f.write(s)
