# coding : utf-8

# 参考链接：https://zhuanlan.zhihu.com/p/29809609

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
	target = "https://www.biqukan.com/1_1094/5403177.html"
	req = requests.get(url=target)
	html = req.text
	bf = BeautifulSoup(html, "html.parser")
	texts = bf.find_all('div',{'class':'showtxt'})
	print (texts[0].text.replace('\xa0'*8,'\n\n'))
	# &nbsp;在html中是用来表示空格的。replace('\xa0'*8,'\n\n')就是去掉下图的八个空格符号，并用回车代替
	
