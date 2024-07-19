# t=('hello',[1,2,3],'world','python')
# print(t)
# t=tuple('helloworld')
# print(t)
# t=tuple([1,2,2,3])
# print(t,type(t))
# print('1是否在元组t中:',1 in t)
# print('最大值:',max(t))
# print('最小值:',min(t))
# print('len:',len(t))
# print('t.index:',t.index(3))
# print('t.count:',t.count(2))

# t=(3)
# print(t,type(t))# 若只有一个元素，逗号不能省
# del t
# print(t)


# t=('hello','world','python')
# print(t[0])
# print(t[0:3:2])
#
# for item in t:
#     print(item)
#
# for i in range(len(t)):
#     print(i,t[i])
#
# for index,item in enumerate(t,start=1):
#     print(index,'--->',item)

t=(i for i in range(1,4))
print(t)  # 生成器对象
t=tuple(t)  # 转换为元组
print(t)

# for item in tuple(t):    # 遍历，相当于取出，遍历后t内无元素
#     print(item)

# print(t.__next__())
# print(t.__next__())   # 将元素取出
# print(t.__next__())
# t=tuple(t)
# print(t)









