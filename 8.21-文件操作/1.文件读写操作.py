def my_write():
    file=open('w.txt','w',encoding='utf_8')
    file.write('hello world')
    file.close()

def my_read():
    file=open('w.txt','r',encoding='utf_8')
    s=file.read()
    print(type(s))
    print(s)


if __name__ == '__main__':
    # my_write()
    my_read()



