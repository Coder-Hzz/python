# 列表是可变数据类型，列表中的元素是不可变数据类型

# lst=['hello','world',66,6.2]
# print(lst)
# print(len(lst))

# lst2=list('helloworld')
# print(lst2)
# print(len(lst2))
# print(max(lst2))
# print(min(lst2))
# print(lst2.count('o'))
# print(lst2.index('o'))


# lst3=list(range(1,10,2))
# print(lst+lst2+lst3)
# print(len(lst3))
# print(max(lst3))
# print(min(lst3))

# lst4=[1,2,3]
# del lst4
# print(lst4)


lst=['hello','world','python']
# for item in lst:
#     print(item)
#
# for i in range(0,len(lst)):
#     print(i,'-->',lst[i])
#
# for index,item in enumerate(lst):#index:序号，不是索引
#     print(index,item)
#
# for index,item in enumerate(lst,start=1):
#     print(index,item)

for index, item in enumerate(lst,1):
     print(index, item)

     