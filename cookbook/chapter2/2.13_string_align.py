text = 'Hello Ajioy'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 填充
print(text.rjust(20, '='))
print(text.center(20, '*'))

# format()
print(format(text, '>20')) # 右对齐
print(format(text, '<20')) # 左对齐
print(format(text, '^20')) # 居中

# 填充字符
print(format(text, '=>20')) # 右对齐
print(format(text, '*^20')) # 左对齐

# 格式化多个值
res = '{:>10s} {:>10s}'.format('Hello', 'Ajioy')
print(res)

x = 1.2345
res = format(x, '>10')
print(res)
res = format(x, '^10.2f')
print(res)

# 在老代码中经常看到%操作符来格式化文本，在新版中，应优先选择format()函数dsfadfddfadsfasdfasdfasdfasdfas
# 更强大，更通用
print('%-20s' % text)
print('%20s' % text)

