# 1.创建类
class Cat:
    def eat(self):
        print('猫吃鱼')
class Dog:
    def eat(self):
        print('狗吃骨')
# 2.创建函数
def fun(obj):
    obj.eat()
# 3.创建对象
cat=Cat()
dog=Dog()
# 4.调用函数
fun(cat)
fun(dog)


