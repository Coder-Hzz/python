lst=[]
s=input('请输入字符串:')
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        lst.append(s[i:j])

lst2=[]
for item in lst:
    lst1=[]
    i = 0
    while i < len(item):
        if item[i] not in lst1:
            lst1.append(item[i])
            i+=1
        else:
            break
    lst2.append(''.join(lst1))

# print(lst2)
print(len(max(lst2,key=len)))

