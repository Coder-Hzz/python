import requests
import re

# 爬取数据
def get_html():
    url='http://www.weather.com.cn/weather1d/101010100.shtml'
    resp=requests.get(url)
    resp.encoding='utf-8'
    return resp.text

# 解析数据
def parse_html(html_str):
    city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',html_str)
    weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',html_str)
    wd=re.findall('<span class="wd">(.*)</span>',html_str)
    zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',html_str)

    lst=[]
    for a,b,c,d in zip(city,weather,wd,zs):
        lst.append([a,b,c,d])
    return lst
