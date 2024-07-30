import time
# now=time.time()  # 时间戳
# print(now)
# # 1722335964.3801415
#
t1=time.localtime()
# print(type(t1))   # <class 'time.struct_time'>   # struct_time对象
print(t1)  # 星期+1
# time.struct_time(tm_year=2024, tm_mon=7, tm_mday=30, tm_hour=18, tm_min=39, tm_sec=24, tm_wday=1, tm_yday=212, tm_isdst=0)

t2=time.localtime(60)
print(t2)
# print(type(t2))
# print('年:',t2.tm_year)
# print('月:',t2.tm_mon)
# print('日:',t2.tm_mday)
# print('时:',t2.tm_hour)
# print('分:',t2.tm_min)
# print('秒:',t2.tm_sec)
# print('星期:',t2.tm_wday)
# print('第几天:',t2.tm_yday)

# print(type(time.ctime()))  # str   时间戳对应的易读字符串
print(time.ctime())
# # Tue Jul 30 18:39:24 2024

print(time.strftime('%Y-%m-%d',time.localtime()))
print(time.strftime('%H:%M:%S',time.localtime()))
print(time.strftime('%A',time.localtime()))
print(time.strftime('%B',time.localtime()))
print(time.strptime('2024-04-03','%Y-%m-%d'))

time.sleep(5)

print('bike')

