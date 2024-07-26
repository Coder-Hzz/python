def lu(s):
    lst=[]
    for item in s:
        if 'A'<=item<='Z':
            lst.append(chr(ord(item)+32))
        elif 'a'<=item<='z':
            lst.append(chr(ord(item)-32))
        else:
            lst.append(item)
    # return lst
    return ''.join(lst)
s=input('请输入要转换的字符串:')
s1=lu(s)
print(s1)





