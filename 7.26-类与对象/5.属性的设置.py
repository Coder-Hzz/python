class Student:
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    @property  # 将方法改成属性使用  只能查看，不能更改
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,value):
        if value!='男' and value!='女':
            print('设置错误，已设为默认值男')
            self.__gender='男'
        else:
            self.__gender=value


stu=Student('旺财','男')
# print(stu.name,'的性别是',stu.gender)

# stu.gender='其他'
# print(stu.name,'的性别是',stu.gender)

stu.gender='女'
print(stu.name,'的性别是',stu.gender)
