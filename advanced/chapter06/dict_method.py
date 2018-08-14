a = {"ajioy1": {"company": "Google"},
     "ajioy2": {"company": "Facebook"}}

b = {"ajioy1": {"company": "Google"},
     "ajioy2": {"company": "Facebook"}}
#a.clear()

# copy，返回浅拷贝，副作用是，一旦任意一方改变指向内容，其他引用的地方也会跟着变
new_dict = a.copy()
new_dict["ajioy1"]["company"] = "Tecent"
print(new_dict)
print(a)

# 深拷贝，完全复制
import copy
new_dict = copy.deepcopy(b)
new_dict["ajioy2"]["company"] = "Neteasy"
print(b)
print(new_dict)
# deepcopy，返回深拷贝

# fromkeys
new_list = ["ajioy1", "ajioy2"]
new_dict = dict.fromkeys(new_list, {"company": "Google"})
print(new_dict)

# get，增强取值操作
# 当没有这个值时，将触发KeyError错误
# new_dict["ajioy"] # 不存在这个key,ＫeyValue
value = new_dict.get("ajioy", {})
# 当key不存在时，返回一个默认值
print(value)

# items
for key, value in new_dict.items():
    print(key, value)

# sefdefault
# D.setdefault(k[,d])-> D.get(k,d), also set D[k] = d if not in D
# 除了取值，还会设置默认值
# 当某一个key不存在时，先取默认值，再将这个值写入dict当中

default_value = new_dict.setdefault("ajioy", "Twitter")
print(default_value)

# update
# 可迭代类型都支持
new_dict.update({"ajioy3": "NetEasy", "ajioy4": "Xunlei"}) # dict
new_dict.update(ajioy="Zhihu", soctte="Quora") #
new_dict.update([("ajioy5", "Apple"),]) # list
new_dict.update((("ajioy6", "Apple"),)) # tuple
pass