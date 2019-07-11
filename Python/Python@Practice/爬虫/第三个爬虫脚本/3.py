# coding : utf-8

# 参考链接：https://zhuanlan.zhihu.com/p/29809609

import sys
import requests
from bs4 import BeautifulSoup

"""
类说明：下载《笔趣看》网小说《一念永恒》
Parameters:
	无
Returns:
	无
Modify:
	2019-03-19
"""

class downloader(object):

	def __init__(self):
		self.server = "https://www.biqukan.com/"
		self.target = "https://www.biqukan.com/1_1094/"
		self.names = []    # 存放章节名
		self.urls = []     # 存放章节链接
		self.nums=0        # 章节数

	"""
	函数说明:获取下载链接
		Parameters:
			无
		Returns:
			无
		Modify:
			2019-03-19
	"""

	def get_download_url(self):
		req = requests.get(url=self.target)
		html = req.text
		div_bf = BeautifulSoup(html, "html.parser")
		div = div_bf.find_all('div',{'class':'listmain'})
		a_bf = BeautifulSoup(str(div[0]))
		a = a_bf.find_all('a')
		self.nums = len(a[15:])
		for each in a[15:]:
			self.names.append(each.string)
			self.urls.append(self.server + each.get('href'))
		
	"""
	函数说明:获取章节内容
		Parameters:
			target - 下载链接(string)
		Returns:
			texts - 章节内容(string)
		Modify:
			2019-03-19
	"""

	def get_contents(self, target):
		req = requests.get(url=self.target)
		html = req.text
		bf = BeautifulSoup(html, "html.parser")
		texts = bf.find_all('div',{'class':'showtxt'})
		texts = texts[0].text.replace('\xa0'*8,'\n\n')
		return texts
	
	"""
	函数说明:将爬取的文章内容写入文件
		Parameters:
			name - 章节名称(string)
			path - 当前路径下,小说保存名称(string)
			text - 章节内容(string)
		Returns:
			无
		Modify:
			2019-03-19
	"""

	def writer(self, name , path ,text):
		write_flag = True
		with open (path, 'a', encoding='utf-8') as f :
			f.write(name + '\n')
			f.writelines(text)
			f.write('\n\n')
	
if __name__ == "__main__":
	d1 = downloader()
	d1.get_download_url()
	print ("《一年永恒》开始下载：")
	for i in range (d1.nums):
		d1.writer(d1.names[i],'一念永恒.txt',d1.get_contents(d1.urls[i]))
		sys.stdout.write("已下载：%.3f%%" % float(i/d1.nums)+'\r')
		sys.stdout.flush()
	print ("《一年永恒》下载完成")
