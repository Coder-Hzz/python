class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

a=A()
b=B()
# 变量的赋值
c=C(a,b)
c1=c
print(c,'对象:',c.n1,c.n2)
print(c1,'对象:',c1.n1,c1.n2)  # c1未开辟新空间
print('-'*30)

# 类对象的浅拷贝
import copy
c2=copy.copy(c)
print(c,'对象:',c.n1,c.n2)
print(c2,'对象:',c2.n1,c2.n2)  # 浅拷贝c2开辟新空间存放c2,对象地址不变，指向原对象
print('-'*30)

# 类对象的深拷贝
c3=copy.deepcopy(c)
print(c,'对象:',c.n1,c.n2)
print(c3,'对象:',c3.n1,c3.n2)  # 深拷贝c3开辟新空间存放c3,创建新的对象

