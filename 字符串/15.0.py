# name='小明'
# age=18
# score=99.5
# print('姓名:%s,年龄:%d,成绩:%f'%(name,age,score))
# print('姓名:%s,年龄:%d,成绩:%.1f'%(name,age,score))
# print('姓名:{0},年龄:{1},成绩:{2}'.format(name,age,score))
# print(f'姓名:{name},年龄:{age},成绩:{score}')

# s='helloworld'
# print(s.find('o'))
# print(s.count('o'))
# print(s.center(20,'*'))

# s=' dl  hello   world   '
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s.rsplit())
# s='le-world'
# print(s.strip('ld'))
# print(s.lstrip('ld'))

# s='hellodsworld'
# print('{0:*<20}'.format(s))
# print('{0:*>20}'.format(s))

# print('{0:,}'.format(12345678))
# print('{0:,}'.format(1234.56))
# print('{0:.2f}'.format(3.1415))
# print('{0:.5}'.format('helloworld'))

# a=452
# print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x}'.format(a))
#
# b=3.14159
# print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))


s='今天要早点睡觉'
scode=s.encode(errors='replace')  # 默认是utf—8，中文占三个字节
print(scode)

scode_gbk=s.encode('gbk',errors='replace')   # gbk中文占两个字节
print(scode_gbk)


# s2='耶☽'
# s2_gbk=s2.encode('gbk',errors='ignore')
# print(s2_gbk)
# s2code_gbk=s2.encode('gbk',errors='replace')
# print(s2code_gbk)
# s2code_gbk=s2.encode('gbk',errors='strict')
# print(s2code_gbk)

print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf_8'))





