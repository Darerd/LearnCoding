# coding : utf-8

import requests
import urllib
# 调用urllib模块下载图片
from bs4 import BeautifulSoup

if __name__ == '__main__':
	req=requests.get('https://darerd.github.io/2019/03/20/%E3%80%8A%E4%B8%8A%E7%98%BE%E3%80%8B%EF%BC%9A%E8%AE%A9%E7%94%A8%E6%88%B7%E5%85%BB%E6%88%90%E4%BD%BF%E7%94%A8%E4%B9%A0%E6%83%AF%E7%9A%84%E5%9B%9B%E5%A4%A7%E4%BA%A7%E5%93%81%E9%80%BB%E8%BE%91-%E4%BA%A7%E5%93%81%E4%B9%A6%E5%8D%95-%E7%AC%AC%E4%BA%8C%E6%9C%9F/#more')
	req.encoding=req.apparent_encoding
	html=req.text
	bs=BeautifulSoup(html,'html.parser')
	img = bs.find_all('img')
	# 得到所有的img标签下的内容
	x=1
	for i in img :
		imgsrc = i.get ('src')
		# 得到img标签下的src
		urllib.request.urlretrieve(imgsrc,'./%s.jpg' %x)
		# 利用urllib.request.urlretrieve下载图片，需要用到urllib模块
		x=x+1
		print ('正在下载: %d '%x)
		