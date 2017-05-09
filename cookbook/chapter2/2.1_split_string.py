line = "asdf dfkdl; afes, dfask, gdfs, foo"
# string.split只适应简单的字符串分割，不允许有多个分隔符
import re
# 正则分割
res = re.split(r'[;,\s]\s*', line) # \s-空格字符 *匹配前一字符0次或无限次
print(res)
# ['asdf', 'dfkdl', 'afes', 'dfask', 'gdfs', 'foo']
# 如果使用了括号捕获分组，被匹配的文本也会在结果集中，如下
fields = re.split(r'(;|,|\s)\s*', line) # | 代表左右表达式匹配任意一个,不太懂
print(fields)
# ['asdf', ' ', 'dfkdl', ';', 'afes', ',', 'dfask', ',', 'gdfs', ',', 'foo']

values = fields[::2] # 切片，步长，每2个取1个
print(len(fields))
print(values)
delimiters = fields[1::2] + [''] # 从[1]开始，每2个取1个
print(delimiters)
print(''.join(v+d for v, d in zip(values, delimiters)))
# 不保留分割字符串
fields = re.split(r'(?:,|;|\s)\s*', line) # 不太懂
print(fields)
print(zip(values, delimiters))
for v, d in zip(values, delimiters):
    print(v, "***", d)
