class Insto:
    def plsy(self):
        pass

class Erhu(Insto):
    def play(self):
        print('二胡')
class Violin(Insto):
    def play(self):
        print('小提琴')
def p(obj):
    obj.play()

e=Erhu()
v=Violin()

p(e)
p(v)











