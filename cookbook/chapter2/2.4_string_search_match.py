# 匹配字面字符串，str.find(), str.endswith(), str.startswidth()
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

# 复杂的匹配用正则和re模块
text1 = '11/27/2014'
text2 = 'Nov 27, 2014'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')


if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# 用同一个模式做多次匹配，先将模式字符预编译为模式对象
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# match总是从字符串开始去匹配，findall是从字符串任意位置开始
m = datepat.match('11/27/2014abcdefg')
print(m.group())
m = datepat.match('abcde11/27/2014')
print(m)
# findall会以列表方式返回所有匹配
text = 'Today is 11/27/2014. Python learn starts 3/13/2014.'
print(datepat.findall(text)) # ['11/27/2014', '3/13/2014']#

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2014')
print(m)
print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

month, day, year = m.groups()
print(month, day, year)

print(datepat.findall(text)) # [('11', '27', '2014'), ('3', '13', '2014')]

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))


