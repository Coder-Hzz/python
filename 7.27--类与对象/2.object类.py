class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'姓名:{self.name},年龄:{self.age}')

    def __str__(self):
        return '重写输出对象的描述信息'

per=Person('bike',20)      # 创建对象时会自动调用__init__函数
print(dir(per))
# 其余属性从父类object类中继承
# 先调用__new__用于创建对象
# 然后手动调用__init__用于初始化对象
# __str__:返回对象的描述信息
print(per)  # 自动调用__str__输出对象的描述信息
per.__str__()
print(per.__str__())
# print(per.__dict__)
# per.show()







