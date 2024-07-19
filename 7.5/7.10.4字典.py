# 创建字典，字典中的键是无序的。字典无整数索引.字典是可变数据类型

# d={10:'cat',20:'dog',30:'pet',20:'zoo'}
# print(d)



# lst1=[10,20,30,40]
# lst2=['cat','dog','pet','zoo','car']
# zipobj=zip(lst1,lst2)
# print(zipobj)
# # print(list(zipobj))   # 将映射对象转成列表类型
#                         # 列表中的元素是一个元组类型
# d=dict(zipobj)          # 真正的字典类型
# print(d)         # 真正的字典类型

# d=dict(cat=10,dog=20)
# print(d)
#
# t=(10,20,30)  # 圆括号元组，不可变数据类型
# print({t:10})

# lst=[10,20,30]    #   方括号列表，可变数据类型   列表不可以作为字典中的键
# print({lst:10})

# 字典属于序列  可求最大值，最小值，长度等
# print(len(d))
# print(len({t:10}))
# print('max:',max(d))
# print('max:',max({t:10}))
# 字典的删除
# del(d)
# print(d)


d={'hello':10,'world':20,'python':30}
# print(d['hello'])
print(d.get('hello'))
# # print(d['hi'])
# print(d.get('hi'))
print(d.get('hi','不存在'))

# for item in d.items():
#     print(item)
#
# for key,value in d.items():
#     print(key,'--->',value)










