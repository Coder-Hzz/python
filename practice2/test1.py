def str(ret):
    if(ret[0]=='#'):
        return ''
    lst=[]
    for i in range(len(ret)):
        if ret[i]!='#':
            lst.append(ret[i])
        else:
            lst.pop()
        i+=1
    ret=''.join(lst)
    return ret

def cmpa(s,t):
    if s==t:
        return True
    else:
        return False

s=str(input('请输入第一个字符串s:'))
t=str(input('请输入第二个字符串t:'))
print(cmpa(s,t))
