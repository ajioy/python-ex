# array, deque
# 数组是连续的空间
import array
# array只能存取指定的数据类型
my_array = array.array("i")
my_array.append(1)
my_array.append("abc") # TypeError: an integer is required (got type str)
