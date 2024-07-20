strs = ['flower','flowers','flight']
# strs = ['give','gives','given']
list1=[]
for i in range(len(strs)):
    list1.append(len(strs[i]))
min=min(list1)
# print(min)
for i in range(1,min):
    if strs[0][0:1] != strs[1][0:1] or strs[1][0:1] != strs[2][0:1]:
        print("")
        break
    elif strs[0][0:i]==strs[1][0:i] and strs[1][0:i]==strs[2][0:i]:
        i+=1
    else:
        print(strs[0][0:i-1])
        print(i-1)
        break

