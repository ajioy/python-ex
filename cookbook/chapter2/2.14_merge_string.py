parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
a = "hello"
b = "ajioy"
print(a+' ' + b)
print('{},{}'.format(a,b))
a = "Hello" "World"
print(a)

# 这种方法要运行的慢一些
s = ''
for p in parts:
    s += p
print(s)

# 用生成器表达式的效率高
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

c = "you r good boy"
print(a+':'+b+':'+c) # ugly
print(':'.join([a, b, c])) # still ugly
print(a, b, c, sep=':') # better

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(sample())
print(text)

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)

with open('E:/hello.txt', 'w') as f:
        for part in combine(sample(), 32768):
            f.write(part)
