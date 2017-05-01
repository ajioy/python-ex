'''
OrderedDict内部维护了一个双向链表，其大小是普通字典的2倍多
'''
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

import json
json_d = json.dumps(d)
print(json_d)


