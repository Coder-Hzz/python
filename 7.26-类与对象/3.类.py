class Dog():  # 创建类
    typ='狗'  # 类变量

    # 构造方法，用于初始化变量
    # 可设置变量默认值
    def __init__(self,name,age,sex='雌'):
        self.name=name
        self.age=age

    # 实例方法
    # def out(self):
    #     print('姓名:{0},年龄:{1},类别:{2}'.format(self.name, self.age, Dog.typ))
    # def speak(self,sound):
    #     print(f'{self.name}的叫声为{sound}')

    # 类方法
    # @classmethod
    # def cm(cls,count):
    #     print(cls.typ*count)

    # 静态方法
    # @staticmethod
    # def sm():
    #     print('静态方法')
    #     静态方法不能调用实例属性和实例方法


# 创建对象
d1=Dog('球球',7)
d2=Dog('毛毛',3)
# d3=Dog('旺财',6)
# lst=[d1,d2,d3]
# lst2=['wa','wan','wang']
# for item in lst:
    # item.out()

# 动态绑定实例属性
d2.color='白'
print('姓名:{0},年龄:{1},类别:{2},颜色:{3}'.format(d2.name,d2.age,Dog.typ,d2.color))

# 动态绑定方法
def intro():
    print('被动态绑定d2的方法')
d2.fun=intro
d2.fun()


# 访问实例变量
# print(f'姓名:{d1.name},年龄:{d1.age},类别:{Dog.typ}')
# print('姓名:{0},年龄:{1},类别:{2}'.format(d1.name,d1.age,Dog.typ))

# d1.out()  # 对象.实例方法
# d1.speak('汪汪')

# print(Dog.cm(3))  # 类名.类方法
# Dog.sm()



