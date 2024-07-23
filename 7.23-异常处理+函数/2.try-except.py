# num1=eval(input('请输入被除数:'))
# num2=eval(input('请输入除数'))
# result=num1/num2
# print(result)
# 先子类，后父类，把最大的异常类型放到最后

# try:
#     num1=eval(input('请输入被除数:'))
#     num2=eval(input('请输入除数'))
#     result=num1/num2
#     # print(result)
# except ZeroDivisionError:
#     print('除数不能为0')
# except NameError:
#     print('未知字符')
# except SyntaxError:
#     print('未知符号')
# except BaseException:
#     print('未知异常')
# else:
#     print('结果:',result)
# finally:  # 无论是否出现异常都会执行
#     print('程序运行结束')


# try:
#     gender=input('请输入您的性别:')
#     if gender!='男'and gender!='女':
#         raise Exception('性别只能是男或女')   # 抛出异常对象
#     # else:
#     #     print('性别:', gender)
# except Exception as e:   # 捕获抛出的异常对象
#     print(e)
# else:
#     print('性别:',gender)





