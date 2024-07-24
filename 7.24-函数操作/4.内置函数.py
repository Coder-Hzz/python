# bool
# print(bool(''))
# print(bool([]))
# print(bool(list()))
# print(bool())
# print(bool(tuple()))
# print(bool(set()))  # 空集合
# print(bool({}))  # 空字典
# print(bool(dict()))
# print(bool(0))
# print(bool(0.0))


# 类型转换
# lst=[12,2,3]
# s=str(lst)
# print(type(s),s)

# print(int(9.8)+int(2.3))
# print(int(9.8)+int('2'))
# print(int(9.8)+int('2.3'))  # ValueError: invalid literal for int() with base 10: '2.3'
# print(float(9.5)+int(3.2))  # 12.5
# print(float('9.5')+int(3.2))  # 12.5
# print(float('9')+int(3.2))  # 12.0
# print(float(9)+float('3'))   # 12.0

# s='hello'
# print(list(s))
# sep=range(1,10)
# print(sep)
# print(type(sep))
# print(tuple(sep))
# print(list(sep))


# 数学函数
# print(abs(100),abs(-100),abs(0))
# print(divmod(5,2))
# print(max('hello'))
# print(min('hello'))
# print(max(1,2,3))
# print(min(1,2,3))
# print(max([15,56]))
# 求和
# print(sum([4,2,6]))
# print(pow(2,3))
# print(round(3.1415))
# print(round(3.1415,2))
# print(round(3.1415,-1))
# print(round(314.15,-1))


# 迭代器操作函数
# (1)sorted
# lst=[6,89,44,15,46,54]
# lst.sort()  # 替换原列表
# print(lst)
# lst1=sorted(lst)  # 创建新列表
# print(lst1)
# lst2=sorted(lst,reverse=True)  # 降序
# lst2=sorted(lst,reverse=False)  # 升序
# print(lst2)

# (2)reversed
# lst3=reversed(lst)
# print(type(lst3))  # <class 'list_reverseiterator'>
# # 迭代器对象，结果不是列表，需要转换为列表/元组才能打印出
# print(list(lst3))
# print(tuple(lst3))

# (3)zip
# x=['a','b','c']
# y=[1,2,3,4]
# zipobj=zip(x,y)
# print(type(zipobj))  # <class 'zip'>
# print(list(zipobj))
# print(tuple(zipobj))

# (4)enumerate
# enum=enumerate(y,start=10)
# print(type(enum))  # <class 'enumerate'>
# print(list(enum))
# print(tuple(enum))

# # (5)all
# lst=[10,20,30,'']
# print(all(lst))  # 全为真-->Ture
# # (6)any
# lst2=[20,'']
# print(any(lst2)) # 全为假-->False

# (7)next
# print(next(zipobj))
# print(next(zipobj))
# print(next(zipobj))


# (8)format
# print(format(3.14,'20'))    # 数字右对齐
# print(format('hello','20')) # 字符左对齐
# print(format('hello','*<20'))  # *:填充符  左对齐
# print(format('hello','*>20'))  # 右对齐
# print(format('hello','*^20'))  # 居中

# print(format(3.14159,'.2f'))
# print(format(20,'b'))
# print(format(20,'o'))
# print(format(20,'d'))
# print(format(20,'x'))
# print(format(20,'X'))


# (9)len
# print(len('str'))
# print(len([10,20]))
# (10)id
# print(id(10))
# print(id('hello'))
# (11)type
# print(type('hello'))
# print(type(10))
# (12)eval
# 去掉两边的符号
# print(eval('10+30'))

