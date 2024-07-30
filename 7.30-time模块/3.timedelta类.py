from datetime import datetime
from datetime import timedelta
t1=datetime(2024,7,30)
t2=datetime(2024,4,3)
delta1=t1-t2
print(type(delta1))
print(delta1)
print(t2+delta1)

td1=timedelta(10)  # 创建一个十天的timedelta对象
print(td1)
td2=timedelta(10,20)  # 十天二十秒
print(td2)




