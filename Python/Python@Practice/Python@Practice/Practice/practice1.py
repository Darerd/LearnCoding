# coding:utf-8
# 使脚本可以识别中文

import requests
from bs4 import BeautifulSoup
# 调用需要的模块
if __name__ == '__main__':
	req=requests.get('https://darerd.github.io/2019/03/20/%E3%80%8A%E4%B8%8A%E7%98%BE%E3%80%8B%EF%BC%9A%E8%AE%A9%E7%94%A8%E6%88%B7%E5%85%BB%E6%88%90%E4%BD%BF%E7%94%A8%E4%B9%A0%E6%83%AF%E7%9A%84%E5%9B%9B%E5%A4%A7%E4%BA%A7%E5%93%81%E9%80%BB%E8%BE%91-%E4%BA%A7%E5%93%81%E4%B9%A6%E5%8D%95-%E7%AC%AC%E4%BA%8C%E6%9C%9F/#more')
	# 得到网站的HTML
	req.encoding=req.apparent_encoding
	#获取文本原来编码，使两者编码一致才能正确显示
	html=req.text
	bs=BeautifulSoup(html,'html.parser')
	# 把HTML文件转为正则文件（我的理解是文本文件）
	texts=bs.find_all('div',{'class':'post-body'})
	# 用find_all函数找到 这样的div文件，其class是post-body
	print(texts[0].text.replace('\xa0'*8,'\n\n'))
	# 用replace函数提出所有的字符、空格等
	
##########
###   还有一个问题：文章的图片怎么下载？？
##########