# filter:通过判断过滤
def fun(num):
    return num%2==1
obj=filter(fun,range(10))  # 函数作为参数，不加括号
print(list(obj))

# map:操作
def upper(x):
    return x.upper()
lst=['hello','world']
obj2=map(upper,lst)
print(list(obj2))

# test2
# def dig2(s):
#     return s.isdigit()
# s=input('请输入字符串:')
# s2=(map(dig2,s))
# print(list(s2))



