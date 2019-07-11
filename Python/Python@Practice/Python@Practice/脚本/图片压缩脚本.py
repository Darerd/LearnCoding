# coding : utf-8

import tinify
import os;

tinify.key = "dcxvBtXsxrMn37RrTYWPK5xhqQ1QWXJd" #自己去申请tinify的开发者key，网址: https://tinypng.com/developers

#获取当前目录
currentDir = os.getcwd()
#压缩的图片类型
supportImgType = ['.jpg','.png'];
#遍历目录下的图片，并批量压缩图片
for item in os.listdir(currentDir):
    if os.path.isfile(item):
        print('doing:'+item) #打印出当前正在压缩的图片名称
        if os.path.splitext(item)[1] in supportImgType:
            source = tinify.from_file(item)
            source.to_file(item)
            print('done:'+item) #打印出压缩完成的图片名称