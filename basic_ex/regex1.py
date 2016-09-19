# coding:utf-8
# regex

import re

try:
    reg = re.match('\d+', 'asdfs123')
    print(reg.group())
except Exception as e:
    print(e)
finally:
    reg2 = re.search('\d+','abc123123')
    print(reg2.group())

    reg3 = re.findall('\d+','145abc1231fas23')
    print(reg3)

    #经过编译，运行速度更快，效果类似于pyc
    reg4 = re.compile('\d+')
    #print(type(reg4))
    print(reg4.findall('145abc1231fas23'))

    reg5 = re.search('(\d+)plus(\d+)equals(\d+)', '12plus23equals25 good')
    print(reg5.group())
    print(reg5.groups())
