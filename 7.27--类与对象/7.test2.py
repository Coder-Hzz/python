class Stu:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def info(self):
        print(self.name,self.age,self.score)


lst=[]
for i in range(1,3):
    s=input(f'请输入第{i}位同学的信息姓名#年龄#得分:').split('#')
    stu=Stu(s[0],s[1],s[2])
    lst.append(stu)
for item in lst:
    item.info()


# lst2=list(lst)
# print(lst2)





