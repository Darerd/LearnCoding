# coding:utf-8

import requests,urllib
from bs4 import BeautifulSoup

if __name__ == '__main__':
	rep = requests.get('https://darerd.github.io/2019/03/21/%E9%9A%8F%E6%83%B3-%E6%96%B0%E9%9B%B6%E5%94%AE%E4%BC%81%E4%B8%9A%E2%80%9C%E2%80%9C%E6%99%BA%E8%83%9C%E2%80%9D%E6%9C%AA%E6%9D%A5/')
	rep.encoding = rep.apparent_encoding
	html = rep.text
	bs = BeautifulSoup(html,'html.parser')
	img = bs.find_all('img')
	# 这个用法参考前面对find_all的使用，可以学习find_all函数怎么用的
	x=1
	for i in img :
		imgsrc = i.get('src')
		urllib.request.urlretrieve(imgsrc,'./%s.jpg' %x)
		x=x+1
		print ('正在下载: %d '%x)
