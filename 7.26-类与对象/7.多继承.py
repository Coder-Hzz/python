class FathA:
    def __init__(self,name):
        self.name=name
    def s1(self):
        print('姓名:',self.name)
class FathB:
    def __init__(self,age):
        self.age=age
    def s2(self):
        print('年龄:',self.age)

class Son(FathA,FathB):
    def __init__(self,name,age,gender):
        FathA.__init__(self,name)
        FathB.__init__(self,age)
        self.gender=gender

son=Son('bike',20,'male')
son.s1()
son.s2()




