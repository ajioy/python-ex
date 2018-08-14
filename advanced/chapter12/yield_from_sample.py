
# final_result = {}
#
# def sales_sum(pro_name):
#     total = 0
#     nums = []
#     while True:
#         x = yield # 只接收值
#         print(pro_name+"销量:", x)
#         if not x:
#             break
#         total += x
#         nums.append(x)
#
#     return total, nums
#
# # 将data_sets中的每行数据进行一个统计
# def middle(key):
#     while True:
#         final_result[key] = yield from sales_sum(key)
#         print(key + "销量统计完成!!!")
#
# def main():
#     # 两层可迭代对象,一是data_sets,二是value,list
#     data_sets = {
#         "ajioy手机": [15000, 18000, 23000],
#         "ajioy平板": [3999, 4041, 5321],
#         "ajioy手表": [23000, 32200, 40000],
#     }
#
#     for key, data_set in data_sets.items():
#         print("start key:", key)
#         m = middle(key)
#         m.send(None) #预激活middle协程
#         # next(m) 跟上面效果一样
#         for value in data_set:
#             m.send(value) # 给协程传递每一组的值
#         m.send(None) # 发送一个标记,让子生成器结束
#
#     print("final_result:", final_result)
#
# if __name__ == "__main__":
#     main()


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield # 只接收值
        print(pro_name+"销量:", x)
        if not x:
            break
        total += x
        nums.append(x)

    return total, nums


if __name__ == "__main__": # yield from可以完成以下所有
    my_gen = sales_sum("ajioy手机")
    my_gen.send(None)
    my_gen.send(1000)
    my_gen.send(2000)
    my_gen.send(4000)
    try:
        my_gen.send(None)
    except StopIteration as e:
        print(e.value)


