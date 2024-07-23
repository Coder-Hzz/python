# test1
# try:
#     score=eval(input('请输入您的分数:'))   # 若输入a，则在此行报错
#     if 0<=score<=100:
#         print('您的分数为:', score)
#     else:
#         raise Exception('请输入1—100间的数字')
# except Exception as e:
#     print(e)
# except NameError:   # 在第二行报错
#     print('请输入数字')


# tset2
# try:
#     a=eval(input('请输入三角形第一边:'))
#     b=eval(input('请输入三角形第二边:'))
#     c=eval(input('请输入三角形第三边:'))
#     if a+b>c and a+c>b and b+c>a:
#         print('能构成三角形，三边长为:',a,b,c)
#     else:
#         # raise Exception(a,b,c,'无法构成三角形')  # 元组
#         raise Exception(f'{a},{b},{c},无法构成三角形')  # 字符串
# except Exception as e:
#     print(e)


