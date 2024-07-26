class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('{0}的年龄是{1}'.format(self.name,self.age))
class Student(Person):
    def __init__(self,name,age,no):
        super().__init__(name,age)
        self.no=no
    def show(self):
        super().show()
        print('学号:',self.no)


class Teacher(Person):
    def __init__(self,name,age,dep):
        super().__init__(name,age)
        self.dep=dep
    def show(self):  # 方法重写
        # super().show()
        # print('部门:',self.dep)  # 子类函数优先级高于父类
        print('{0}的年龄是{1},部门是{2}'.format(self.name, self.age,self.dep))

stu=Student('bike',18,109)
stu.show()
teac=Teacher('大锤',20,'home')
teac.show()


