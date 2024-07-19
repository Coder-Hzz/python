# for i in range(1,4):
#     for j in range(1,5-i):
#         print('*',end='')
#     print( )


# for i in range(1,5):
#     for j in range(1,6-i):
#         print(' ',end='')
#     for k in range(1,2*i):
#         print('*',end='')
#     print( )


# row=eval(input('请输入菱形行数:'))
# while (row+1)%2:
#     print('输入不合法，请重新输入')
#     row=eval(input('请输入菱形行数:'))
# top_row=(row+1)//2
# for i in range(1,top_row+1):
#     for j in range(1,top_row+1-i):
#         print(' ',end='')
#     for k in range(1,2*i):
#         if k==1 or k==2*i-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print( )
# bottom_row=row//2   #下半部分总行数  3
# for l in range(1,bottom_row+1):
#     for m in range(1,l+1):
#         print(' ',end='')
#     for n in range(1,row+1-2*l):
#         if n==1 or n==row-2*l:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()


