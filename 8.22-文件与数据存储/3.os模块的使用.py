import os
# print('当前工作路径:',os.getcwd())
lst=os.listdir()
# print('当前路径下的所有目录及文件:',lst)
# print('指定路径下的所有目录及文件:',os.listdir('D:/Users/LENOVO/PycharmProjects/pythonProject'))
# 创建目录  创建后不可再创建，需注释掉
# os.mkdir('os创建文件夹')
# os.makedirs('./aa/bb/cc')  # 创建多级目录
# 删除文件
# os.rmdir('./os创建文件夹')  #删除后不可再删除，需注释
# os.removedirs('./aa/bb/cc')  # 删除多个目录

# 改变当前的工作路径
# os.chdir('path')  # 文件路径不变，工作（运行）路径改为path  (未运行)
# print('当前工作路径:',os.getcwd())

# 遍历目录树
for dirs,dirlst,filelst in os.walk('D:/Users/LENOVO/PycharmProjects'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('-'*20)
