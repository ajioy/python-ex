a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

# find keys in common
c = a.keys() & b.keys() # {'x','y'}
print(c)

# find keys in a that are not in b
c = a.keys() - b.keys() # {'z'}
print(c)

# find (key, value) pairs in common
c = a.items() & b.items() # {('y':2)}
print(c)

d = a.keys() - {'z', 'w'}
c = {key:a[key] for key in d}
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c) # {'x':1,'y":2}

