# coding:utf-8
# 爬网站：https://www.qiushibaike.com/text/

import requests
from bs4 import BeautifulSoup
import re
if __name__ == '__main__':
	server='https://www.qiushibaike.com'
	page=range(1,6)
	for i in page:
		target=server+'/text/page/'+str(i)
	###以上得到前五页的url
	
	req = requests.get (url=target)
	req.encoding = req.apparent_encoding
	#获取文本原来编码，使两者编码一致才能正确显示
	
	html = req.text
	bf = BeautifulSoup(html,'html.parser')
	### 得到正则表达式
	
	body = bf.body
	
	####从<a>标签中得到其属性的方法，包括href
	for a in body.find_all('a',{'class':'contentHerf'}):
		link = server+a.get('href')
	####从<a>标签中得到其属性的方法，包括href
	
	###得到所有url的文本内容
	req_all = requests.get (url=link)
	req_all.encoding = req_all.apparent_encoding
	html = req_all.text
	bf_all = BeautifulSoup(html,'html.parser')
	body_all = bf_all.body
	texts=body.find_all('div',{'class':'content'})
	###texts 是<class 'bs4.element.ResultSet'>
	###利用print (type(texts)) 可以打印出texts的数据类型
	dr = re.compile(r'<[^>]+>',re.S)
	### 去除所有的html标签
	dd = dr.sub('',str(texts))
	### re.sub 仅支持字符
	### 需要把texts的数据类型转变为字符，利用str()函数
	print(dd)
	#print (type(texts))
	
####还存在一些问题：
### 2. 怎么样去除编译结果中的<span>和<div>等标签