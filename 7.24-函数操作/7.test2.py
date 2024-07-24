# test2

# def dig(s):
#     return s.isdigit()
# s=input('请输入字符串:')
# s1=(filter(dig,s))
# s2=list(s1)
# sum=0
# for i in range(len(s2)):
#     s2[i]=int(s2[i])
#     sum+=s2[i]
# print(list(s2))
# print(sum)


def digsum(s):
    lst=[]
    add=0
    for item in s:
        if item.isdigit():
            lst.append(int(item))
            # sum+=int(item)
    add=sum(lst)
    print(lst)
    print(add)
s = input('请输入字符串:')
digsum(s)

