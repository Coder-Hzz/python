class Cirle:
    def __init__(self,r):
        self.r=r
    def s(self):
        # return 3.14*self.r*self.r
        return 3.14*pow(self.r,2)
    def c(self):
        return 2*3.14*self.r

r=eval(input('请输入圆的半径:'))
# s=Cirle(r).s()
# c=Cirle(r).c()
c1=Cirle(r)
s=c1.s()
c=c1.c()
print('面积:',s)
print('周长:',c)





