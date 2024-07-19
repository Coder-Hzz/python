# d={1:'张三',2:'李四',3:'王五'}
# print(d)

# d[4]='赵七'
# print(d)
# c=d.keys()
# print(c)              # 键
# print(list(c))
# print(tuple(c))

# values=d.values()
# print(values)             # 值
# print(list(values))
# print(tuple(values))
#
# lst=list(d.items())   # 列表类型  （项目（整体））
# print(lst)
#
# d=dict(lst)           # 再转为字典类型
# print(d)

# print(d.pop(1))
# print(d)

# print(d.pop(12,'不存在'))

# print(d.popitem())
# print(d)

# d.clear()
# print(d)
# print(bool(d))

# 字典的生成式
# import random
# d={item:random.randint(1,100) for item in range(4)}
# print(d)

lst1=[1,2,3]
lst2=['张三','李四','王五']
d={key:value for key,value in zip(lst1,lst2)}
print(d)







