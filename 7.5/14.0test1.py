# 千年虫
# lst1=[98,88,95,00,94]
# for i in range (0,len(lst1)):      #  i--->index
#     if str(lst1[i])!='0':
#         lst1[i]='19'+str(lst1[i])
#     else:
#         lst1[i] = '200' + str(lst1[i])
# print(lst1)


# lst=[98,88,95,00,94]
# for index,value in enumerate(lst):
#     if str(value)!='0':
#         lst[index]='19'+str(value)
#     else:
#         lst[index]='200'+str(value)
# print(lst)


# 京东购物流程

# list=[]
# for i in range(5):
#     goods=input('请输入编号和商品:')
#     list.append(goods)
# for item in list:
#     print(item)
# cart=[]
# while True:
#     flag=False
#     num=input('请输入您要买的商品编号:')
#     for item in list:
#         if num==item[0:3]:
#             flag=True
#             cart.append(item)
#             print('商品已添加至购物车')
#             break  # 退出for循环
#     if not flag and num!='q':
#         print('商品不存在')
#     if num=='q':
#         break
# print('您要购买的商品有:',cart)


# list=[]
# for i in range(3):
#     goods=input('请输入商品编号及名称:')
#     list.append(goods)
# # print(list)
# for item in list:
#     print(item)
# cart=[]
# while True:
#     flag=False
#     num=input('请输入您要购买的编号:')
#     for item in list:
#         if num==item[0:3]:
#             flag=True
#             cart.append(item)
#             print('商品已加入购物车')
#             break
#     if not flag and num!='q':
#         print('商品不在列表')
#     if num=='q':
#         break
# cart.reverse()
# # print('您的购物车中有:',cart)
# for item in cart:
#     print (item)


# dic_ticket={
#     '12345':['北京——上海','12:12','13:20','00:45'],
#     'G4567':['上海——杭州','8:20','10:12','00:56'],
#     'T130':['上海——无锡','16:30','17.30','01:00']
# }
# print('车次   出发站——终点站    出发时间     到达时间     总时长')
# for key in dic_ticket.keys():
#     print(key,end='  ')
#     for item in dic_ticket.get(key):
#         print(item,end='  \t\t')
#     print()
#
# train_no=input('请输入选择的车次:')
# info=dic_ticket.get(train_no,'您输入的车次不存在')
# if info!='您输入的车次不存在':
#     s=info[0]+' '+info[1]+'开'
#     person=input('请输入乘车人:')
#     print('您已购买'+train_no+' '+s+',请'+person+'提前安排行程  【中国铁路】')
# else:
#     print(info)



# txl=set()
# for i in range(1,3):
#     info=input(f'请输入第{i}位好友的联系方式:')
#     txl.add(info)
# for item in txl:
#     print(item)














