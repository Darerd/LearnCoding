#-*-coding:utf-8-*-

# 调用模块
import jieba
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
# 读取背景图片信息，设置遮罩
from PIL import Image
import numpy as np

# 导入和读取txt文件
mytext = open(r'python.txt','r').read()

# 读取背景图片信息
back_pic = np.array(Image.open(r'1.png'))		# 图片设置为背景遮罩
image_colors = ImageColorGenerator(back_pic)	# 读取图片的颜色信息

# 结巴分词
mytext = " ".join(jieba.cut(mytext)) 
#print(mytext)

# 设置词云
wordcloud = WordCloud(mask = back_pic,              # 以背景图片设置遮罩
                      font_path = 'simsun.ttf',		# 设置中文字体
	                  background_color = "black",	# 设置背景颜色
	                  max_words = 2000,				# 设置最大显示的字数
	                  max_font_size = 50, 			# 设置字体最大值
	                  random_state = 30,			# 设置有多少种随机生成状态，即有多少种配色方案
	)
# 把文件生成词云
wordcloud = wordcloud.generate(mytext)

# 展示词云图
plt.imshow(wordcloud.recolor(color_func = image_colors),interpolation='bilinear')
plt.axis("off")
plt.show()