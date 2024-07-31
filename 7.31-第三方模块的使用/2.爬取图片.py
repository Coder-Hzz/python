import requests
url='https://www.baidu.com/img/flexible/logo/pc/result.png'
pic=requests.get(url)

with open('pic.png','wb') as file:
    file.write(pic.content)



