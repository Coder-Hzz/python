# 多位置参数
def fun(*para):
    print(type(para))
    for item in para:
        print(type(item))
        print(item)

# fun(10,20,30)
# fun([1,2],[4,5])
# fun([1,2,3])
# fun(*[1,2,3])

# 多关键字参数
def fun2(**kwpara2):
    print(type(kwpara2))
    for key,value in kwpara2.items():
        print(key,'----->',value)

# fun2(name='hz',age=18)

# d={'name':'hz','age':18}
# fun2(d)   # TypeError: fun2() takes 0 positional arguments but 1 was given  0位置参数
# fun2(**d)   # **:系列解包操作



