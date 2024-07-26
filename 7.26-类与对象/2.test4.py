def ins(l,s):
    for item in lst:
        if s==item:
            return True
    # else:
    return False
lst=['hello','world','hi']
s=input('请输入要查找的字符串:')
result=ins(lst,s)
print('存在' if result else '不存在')

