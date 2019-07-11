# coding:utf-8

import requests
from bs4 import BeautifulSoup
import re

####获取百度贴吧页码的方法
server = 'https://tieba.baidu.com/p/3138733512'
i = input('只看楼主，输入：1，否则输入：0 >' )
seeLZ = '?see_lz=' + str(i)
req = requests.get (url=server+seeLZ)
req.encoding = req.apparent_encoding
html = req.text
bf = BeautifulSoup(html,'html.parser')
body = bf.body
data = body.find('div', {'id': 'thread_theme_5'})
##data是list格式
ul = data.find('ul')
li = ul.find_all('li')
###li和ul也是list格式
for page in li:
	num = page.find_all('a')
	##得到<a>标签的内容
	print (num[3].string)
	# print (num[3])
# 可以注意下上面两种打印出来的 num[3]的结果
## num[3]后加.string可以得到标签内的字符内容
	

