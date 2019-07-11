# coding:utf-8

# selenium操作测试代码
# selenium文档：http://www.testclass.net/selenium_python

from selenium import webdriver
# 从selenium调用webdriver模块

driver = webdriver.Chrome()
# 打开Chrome浏览器
driver.get('https://www.baidu.com/')
# 打开指定的URL

#driver.find_element_by_name('wd')
# seleniu定位元素
# 参考资料：http://www.testclass.net/selenium_python/find-element
#clear() :  清除文本
# 以上两句代码可以合并为：
driver.find_element_by_name('wd').clear()

driver.find_element_by_id('kw').send_keys('Python')
# send_keys(value) :模拟按键输入

driver.find_element_by_class_name('bg s_btn').click()
# click() :单击元素



driver.quit()
