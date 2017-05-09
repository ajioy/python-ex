# 用指定的列宽格式化长字符串
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 70))
'''
Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around the eyes, look into my eyes,
you're under.
'''
print(50 * '-')
print(textwrap.fill(s, 40))
print(50 * '-')
print(textwrap.fill(s, 40, initial_indent='        '))
'''
    Look into my eyes, look into my
eyes, the eyes, the eyes, the eyes, not
around the eyes, don't look around the
eyes, look into my eyes, you're under.
'''
print(50 * '-')
print(textwrap.fill(s, 40, subsequent_indent='        '))
'''
Look into my eyes, look into my eyes,
    the eyes, the eyes, the eyes, not
    around the eyes, don't look around
    the eyes, look into my eyes, you're
    under.
'''

import os
print(os.get_terminal_size().columns)
