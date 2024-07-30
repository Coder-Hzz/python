from datetime import datetime  # 从datetime模块中导入datetime类

t1=datetime.now()
print('当前系统时间:',t1)
# print(type(t1))  # <class 'datetime.datetime'>

t2=datetime(2024,4,3,10,26,30)
# print(type(t2))   # <class 'datetime.datetime'>
print('t2:',t2)  # 默认格式
# print('年:',t2.year,'月:',t2.month,'日:',t2.day)
# print('时:',t2.hour,'分:',t2.minute,'秒:',t2.second,'微秒:',t2.microsecond)
# print(f'{t2.year}年')
# print('{0}年{1}月{2}日'.format(t2.year,t2.month,t2.day))
# # 比较
# print('t1早于t2吗?',t1<t2)

t3=datetime.strftime(t2,'%Y/%m/%d %H:%M:%S')  # str
print('t3:',t3)
t4=datetime.strptime(t3,'%Y/%m/%d %H:%M:%S')  # <class 'datetime.datetime'> (时间，格式)
print('t4:',t4)

t5=datetime.strftime(t2,'%Y年%m月%d日 %H时%M分%S秒')
print('t5:',t5)
t6=datetime.strptime(t5,'%Y年%m月%d日 %H时%M分%S秒')
print('t6:',t6)




