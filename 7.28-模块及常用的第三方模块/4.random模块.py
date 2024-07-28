import random
random.seed(10)  # 随机种子
print(random.random())
print(random.random())
print(random.randint(1,100))  # [1,100]
print(random.uniform(1,10))  # [1,10]
# for i in range(10):
#     print(random.randrange(1,10,3))  #  [1,10)步长为3   1,4,7随机输出

lst=[i for i in range(1,10)]
print(random.choice(lst))
# 随机排序
random.shuffle(lst)
print(lst)

random.shuffle(lst)
print(lst)





