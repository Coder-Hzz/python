# def add(x,y):
#     return x+y
# s=add(add(1,2),3)
# print(s)

def add(x,y):
    return x,y,x+y
# s=add(1,2)
# print(s)
# print(type(s))
# a,b,c=s
a,b,c=add(1,2)
print(a)
print(b)
print(c)




