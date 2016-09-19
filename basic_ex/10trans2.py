# coding:utf-8
#10进制转2进制


def Trans(num, redix = 2):
    i = 0
    list = []
    while num != 0:
        list.append(num % redix)
        num = num / redix
        i += 1
    return list

res = Trans(50)
res.reverse()
print res