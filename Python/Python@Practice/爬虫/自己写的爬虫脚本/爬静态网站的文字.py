# coding:utf-8
# 爬网站：http://www.hbrchina.org/

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
	target = "http://www.hbrchina.org/2019-02-18/7150.html"
	req = requests.get (url=target)
	req.encoding = req.apparent_encoding
	#获取文本原来编码，使两者编码一致才能正确显示
	html = req.text
	bf = BeautifulSoup(html,'html.parser')
	body = bf.body
	texts = body.find_all ('div',{'class':'article-content'})
	print(texts[0].text.replace('\xa0'*8,'\n\n'))