def my_write():  # 一维数据
    lst=['张三','李四','王五']
    with open ('student.csv','w') as file:
        # csv:逗号分隔值
        file.write(','.join(lst))
        # 列表转成字符串

def my_read():
    with open('student.csv','r') as file:
        s=file.read()
        lst=s.split(',')
        print(lst)

def my_write_table():   # 二维数据
    lst=[
        ['水果','单价','个数'],
        ['苹果','8.2','6'],
        ['香蕉','4.5','4']
    ]
    with open('table.csv','w',encoding='utf-8') as file:
        for item in lst:
            line=','.join(item)
            file.write(line)
            file.write('\n')

def my_read_table():
    data=[]
    with open('table.csv','r',encoding='utf-8') as file:
        lst=file.readlines()
        for item in lst:
            data.append(item[:len(item)-1].split(','))
        print(data)




if __name__ == '__main__':
    # my_write()
    # my_read()
    # my_write_table()
    my_read_table()
