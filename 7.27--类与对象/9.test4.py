class Car:
    def __init__(self,type,no):
        self.type=type
        self.no=no
    def start(self):
        print('开始')
    def end(self):
        print('结束')
class Taxi(Car):
    def __init__(self,type,no,dep):
        super().__init__(type,no)
        self.dep=dep
    def start(self):
        print(f'类型:{self.type},车牌号:{self.no},公司:{self.dep}')
    def end(self):
        print('已到站，欢迎下次乘坐')

class Private(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name=name
    def show(self):
        print(f'类型:{self.type},车牌号:{self.no},车主:{self.name}')

taxi=Taxi('出租车','京A888888','didi')
private=Private('私家车','沪A666666','bike')
taxi.start()
taxi.end()
# private.start()
# private.end()
private.show()



