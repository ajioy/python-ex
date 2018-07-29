text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
    ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

from collections import namedtuple
def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, text):
    print(tok)
'''
Token(type='NAME', value='foo')
Token(type='WS', value=' ')
Token(type='EQ', value='=')
Token(type='WS', value=' ')
Token(type='NUM', value='23')
Token(type='WS', value=' ')
Token(type='PLUS', value='+')
Token(type='WS', value=' ')
Token(type='NUM', value='42')
Token(type='WS', value=' ')
Token(type='TIMES', value='*')
Token(type='WS', value=' ')
Token(type='NUM', value='10')
'''

# 剔除空格
print(50 * '-')
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)

PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat = re.compile('|'.join([PRINT, NAME]))
for tok in generate_tokens(master_pat, 'printer'):
    print(tok)


class Cat:
    def __init__(self, a, b):
        _a = a
        _b = b

c = Cat.new
