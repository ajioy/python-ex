from fnmatch import fnmatch, fnmatchcase
# fnmatch匹配能力介于简单的字符串方法和强大的正则表达式之间
res = fnmatch('foo.txt', '*.txt')
print(res)
res = fnmatch('foo.txt', '?oo.txt')
print(res)
res = fnmatch('Dat45.csv', 'Dat[0-9]*')
print(res)
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
res = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(res)

res = fnmatch('foo.txt', '*.TXT')
print(res)
# 区分大小写
res = fnmatchcase('foo.txt', '*.TXT')
print(res)

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

res = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(res)

res = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(res)
