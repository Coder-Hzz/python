import prettytable as pt

def show_ticket(row_num):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(1,row_num+1):
        lst=[f'第{i}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)
def order_ticket(row_num,row,col):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(1,row_num+1):
        if i==int(row):
            lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(col)]='已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)

if __name__ == '__main__':
    row_num=6
    show_ticket(row_num)
    choice=input('请输入要选择的座位号[*,*]:')
    row,col=choice.split(',')  # 系列解包赋值
    order_ticket(row_num, row, col)



