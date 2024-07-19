# lst=[5,66,565,44,4554,54]
# print('原列表:',lst)
#
# lst.sort()
# print('升序:',lst)
#
# lst.sort(reverse=True)
# print('降序:',lst)
# print(lst)

# lst2=['banana','apple','Cat','Orange']
# print('原列表:',lst2)
# lst2.sort()
# print('升序:',lst2)
# lst2.sort(reverse=True)
# print('降序:',lst2)

# 自己指定规则
# lst2.sort(key=str.lower)  # lower是参数，参数后不加括号，调用才加括号
# print('都为小写:',lst2)


lst=['banana','apple','Cat','Orange']
print('原列表:',lst)

asc_lst=sorted(lst)
print('升序:',asc_lst)

# desc_lst=sorted(lst,reverse=True)
# print('降序:',desc_lst)
# print(lst)

asc_lst=sorted(lst,key=str.lower)
print('升序:',asc_lst)
asc_lst=sorted(lst,key=str.upper)
print('升序:',ascf_lst)

