# coding:utf-8

from selenium import webdriver
import re 

driver = webdriver.Chrome()
# 打开Chrome浏览器
url = 'https://movie.douban.com/explore#!type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0'
print ("爬取豆瓣电影")
driver.get(url)
content = driver.find_elements_by_xpath("//div[@class='list']")
for ambition in content:
	print (ambition.text)
