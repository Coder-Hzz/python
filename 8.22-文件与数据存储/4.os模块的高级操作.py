import os

# 删除文件
# os.remove('stu.txt')  仅供一次操作

# 重命名文件
# os.rename('./stu.txt','new_stu.txt')

# 转换时间格式
import time
def data_format(longtime):
    s=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))
    return s

# 获取文件信息
info=os.stat('./new_stu.txt')
# print(type(info))
# print(info)

print('最后一次访问时间:',data_format(info.st_atime))
print('win系统中文件创建时间:',data_format(info.st_ctime))
print('最后一次修改时间:',data_format(info.st_mtime))
print('文件大小(单位是字节):',info.st_size)

# 启动路径下的文件
# os.startfile('calc.exe')

# 启动Python解释器
# os.startfile(r'C:\Users\LENOVO\AppData\Local\Programs\Python\Python311\python.exe')



