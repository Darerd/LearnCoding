# coding:utf-8
###去除html标签的方法

import re
html='<span href="//www.jb51.net"脚本之家</span>,Python学习！'
dr = re.compile('<span>|</span>')
### 去除字符中标签<span>和</span>
dr = re.compile('<a.*?>|</a>')
### 去除字符中标签<a>xxxxx</a> 中的所有内容，包括<a>和</a>
dr = re.compile(r'<[^>]+>',re.S)
### 去除所有的html标签,因为html标签，会有这个符号<>
dd = dr.sub('',html)
print(dd)