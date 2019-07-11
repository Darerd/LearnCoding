# coding:utf-8

import requests
from bs4 import BeautifulSoup
import re

server = 'https://tieba.baidu.com/p/3138733512'
i = input('只看楼主，输入：1，否则输入：0 >' )
seeLZ = '?see_lz=' + str(i)
for num in range(0,5):
	num = num+1
target = server + seeLZ + '&pn=' + str(num)
#print (target)

req = requests.get (url=target)
req.encoding = req.apparent_encoding
html = req.text
bf = BeautifulSoup(html,'html.parser')
body = bf.body
post = body.find_all('div',{'class':'p_content'})
dr = re.compile(r'<[^>]+>',re.S)
### 去除所有的html标签,因为html标签，会有这个符号<>
dd = dr.sub('',str(post))
# print(dd)

##写入文件
with open('1.txt','a',encoding='utf-8') as file:
	file.write(dd)
	
####存在的问题########
####1. 怎么自动爬取百度贴吧的页码，不需要人工选定页数？？？

