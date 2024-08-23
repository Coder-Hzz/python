import json
lst=[
    {'name': '小红','age':18,'score':95},
    {'name': '小王','age':20,'score':98},
    {'name': '小明','age':17,'score':91}
]
# 编码
s=json.dumps(lst,ensure_ascii=False,indent=4)
#                     正常显示中文       缩进

# print(type(s))
# print(s)

# 解码
lst2=json.loads(s)
# print(type(lst2))
# print(lst2)

# 编码到文件
with open ('stu.txt','w') as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)

# 解码到程序
with open ('stu.txt','r') as file:
    lst3=json.load(file)
    print(type(lst3))
    print(lst3)


