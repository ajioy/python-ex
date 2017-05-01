line = 'nobody:*:-2:-2:unprivileged User:/var/empty:/usr/bin/false'

uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(fields)
print(sh)

''' result
nobody
/var/empty
['*', '-2', '-2', 'unprivileged User']
/usr/bin/false
''' 

# ignore some value, *_
record = ['ajioy', 50, 123.45, (12, 19, 2013)]
name, *_, (*_, year) = record
print(name)
print(year)
