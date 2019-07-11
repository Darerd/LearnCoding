# coding : utf-8

# 参考链接：https://zhuanlan.zhihu.com/p/29809609

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
	server = "https://www.biqukan.com/"
	target = "https://www.biqukan.com/1_1094/"
	req = requests.get(url=target)
	html = req.text
	div_bf = BeautifulSoup(html, "html.parser")
	div = div_bf.find_all('div',{'class':'listmain'})
	a_bf = BeautifulSoup(str(div[0]))
	a = a_bf.find_all('a')
	for each in a:
		print (each.string, server + each.get('href'))
	#print (div[0])
	
