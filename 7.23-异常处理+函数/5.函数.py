# def add(x,y):
#     print(x+y)
# add(10,20)

# s=100
# def add2(x,y):
#     s=200
#     return x+y+s
# # sum=add2(10,20)
# # print(sum)
# print(add2(10,20))
# print(s)

# def add3(i):
#     sum=0
#     for i in range(i+1):
#         sum+=i
#     print(sum)
# add3(10)


# def add4(i):
#     sum=0
#     sum1=0
#     sum2=0
#     for i in range(i+1):
#         if i%2:
#             sum1+=i
#         else:
#             sum2+=i
#         sum+=i
#     print(sum,sum1,sum2)
# add4(10)


# def hello(name,year):
#     print(name,'你好')
#     print(year,'你好')
# hello('hz',2024)
# print('-'*20)
# hello(name='hzz',year=2024)
# hello(year=2024,name='hz')
# hello('hz',year=2024)
# hello(name='hz',2024)  # SyntaxError: positional argument follows keyword argument
# hello(2024,name='hz')   # TypeError: hello() got multiple values for argument 'name'
# 位置参数在前 关键字参数在后

# def hello(name='hz',year=2024):
#     print(name,'你好')
#     print(year,'你好')
# hello()
# 位置参数在前，默认参数在后
# hello(name='hzz',year=2025)
# hello(2025)
# hello(year=2025)
# hello('hzz')
# hello(year=2024)





