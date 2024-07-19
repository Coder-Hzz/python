# 集合中只能存储不可变数据类型
# 与列表，字典一样，是Python中的可变数据类型
# 可以存储字符串，整数，浮点数，元组
# 不能存储字典，不能存储列表
# 列表是可变数据类型，列表中的元素是不可变数据类型

# s={10,20,30}
# print(s)

# s={[1,20],[3,5]}
# print(s)

# s=set()
# print(s,type(s),bool(s))

# s={}
# print(s,type(s))
#
# s=set('hello')
# print(s)

# s2=set([1,2,3])
# print(s2)
# s3={1,2,3}
# print(s3)

# s4=set(range(1,10))
# print(s4)

# print('max:',max(s4))
# print('min:',min(s4))
# print('len:',len(s4))
# print('5在s4中存在吗？',5 in s4)
# del s4
# print(s4)

# s1=set(range(1,10))
# s2=set(range(5,15))
# print(s1&s2)
# print(s1|s2)
# print(s1-s2)  # 差集
# print(s1^s2)  # 补集

s={10,20,30}
# s.add(40)
# print(s)
# s.remove(30)
# print(s)
# s.clear()

# for item in s:
#     print(item)

# for index,item in enumerate(s,start=1):
#     print(index,'--->',item)

# s={i for i in range(1,10)}
# print(s)
# s={i for i in range(1,10) if i%2==1}
# print(s)


# data=eval(input('请输入要匹配的数据:'))
# match data:
#     case {'name':'hz'}:
#         print('字典')
#     case[1,2,3]:
#         print('列表')
#     case(1,2):
#         print('元组')
#     case _:
#         print('else')




