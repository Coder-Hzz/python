def my_write(s):
    file=open('a.txt','a',encoding='utf_8')
    # a:追加
    file.write(s)
    file.write('\n')
    file.close()

def my_write_list(file,lst):
    file1=open(file,'a',encoding='utf_8')
    file1.writelines(lst)
    file1.close()

if __name__ == '__main__':
    # my_write('hello')
    # my_write('world')
    lst=['姓名\t','年龄\n','小红\t','18']
    my_write_list('b.txt',lst)



