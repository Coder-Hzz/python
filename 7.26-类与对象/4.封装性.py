# 私有变量
class Account:
    __rate=0.2  # 私有类变量
    def __init__(self,name,money):
        self.__name=name   # 私有实例变量
        self.money=money
    def out(self):  # 类的内部可以访问私有变量
        print('姓名:{2},金额:{0},利率:{1}'.format(self.money,Account.__rate,self._name))
    def __get(self):   # 私有方法
        print('金额:{0}'.format(self.money))
    def pr(self):
        account.__get()   # 类内部可调用


account=Account('小李',1000)
# account.out()
# print('姓名:{1},金额:{0}'.format(account.money,account._name))
# print('利率:{0}'.format(Account.__rate))
# AttributeError: type object 'Account' has no attribute '__rate'

# 访问私有变量
# print('利率:{0}'.format(account._Account__rate))


# 私有方法
# account._get()
# account.__get()  # 类外部不可调用
# AttributeError: 'Account' object has no attribute '__get'. Did you mean: '__ge__'?
# account.pr()  # 类内部可调用
# account._Account__get()

# 内置函数dir
# print(dir(account))
