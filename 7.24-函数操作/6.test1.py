# test1:
# import random
# lst=[]
# for i in range(10):
#     nums=random.randint(1,100)
#     lst.append(nums)
# print(lst)
# max=lst[0]
# for item in lst:
#     if item>max:
#         max=item
# print(max)


import random
def get_max(lst):
    max=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>max:
            max=lst[i]
    return max
lst=[ random.randint(1,100) for i in range(10)]
print(lst)
print(get_max(lst))



