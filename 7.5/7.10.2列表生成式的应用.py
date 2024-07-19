import random
# lst=[item for item in range(1,11)]
# print(lst)
# lst=[item*item for item in range(1,11)]
# print(lst)
# lst=[random.randint(1,100) for _ in range(1,11)]
# print(lst)

# lst=[i for i in range(1,11) if i%2==0]
# print(lst)
#
# lst=[i for i in range(10) if i%2==0]
# print(lst)


# lst=[
#     ['城市','环比','同比'],
#     ['北京',12,56],
#     ['上海',48,89],
#     ['深圳',56589,52]
# ]
# # print(lst)
# for row in lst:
#     for item in row:
#         print(item,end='\t')
#     print()


lst=[[item for item in range(5)]for row in range(4)]
print(lst)




