import datetime

def input_data():
    inputdate=input('请输入开始日期(eg:20220101):')
    datestr=inputdate[0:4]+'-'+inputdate[4:6]+'-'+inputdate[6:]
    dt=datetime.datetime.strptime(datestr,'%Y-%m-%d')
    return dt

if __name__ == '__main__':
    # print(input_data())
    date=input_data()
    delta=eval(input('请输入时间间隔:'))
    date2=date+datetime.timedelta(days=delta)
    print('推算日期为:',date2)


