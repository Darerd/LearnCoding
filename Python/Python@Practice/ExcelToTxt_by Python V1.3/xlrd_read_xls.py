### 参考链接：https://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html ####


import xlrd
# 读取（read）excel文件内容的模块
### 讲解资料： https://segmentfault.com/a/1190000017485618

#打开文件
workbook = xlrd.open_workbook(r'C:\Users\yuhui\Desktop\PythonToTxt_迭代工作夹\ExcelToTxt_by Python V1.3\123.xlsx')

#获取excel工作表中的sheet表的名称
#workbook.sheet_names()

#根据Sheet名称获取sheet中的所有内容
sheet2 = workbook.sheet_by_name('Sheet2') # 注意Sheet的大小写 

#sheet的名称、行数和列数
#print (sheet2.name,sheet2.nrows,sheet2.ncols)
# 以此为例，输出结果为： Sheet2 128 21

#获取行数和列数
nrows= sheet2.nrows
ncols= sheet2.ncols

# 获取整行和整列的值（list形式）
#rows=sheet2.row_values(0) # 获取第一行内容 # list
#cols=sheet2.col_values(0) # 获取第一列内容 # list
# print (rows,cols)

# 循环行列表数据
#for i in range(nrows):
    #rows = sheet2.row_values(i)
    #print(rows)
# 以上语句有问题的原因：每次赋值给rows的数值，被后面的刷新掉了。

rows = []
# 新建一个空list，用于后面装数据进去
for i in range(nrows):
    v = sheet2.row_values(i)
    # 把sheet2中每一行的值（list值）赋值给 v
    rows.append(v)
    # 把 v 中的值写入到rows（list组成的多维list）
    print(v)
    
# 获取单元格的内容
# 第3行4列的cell写法为：cell(2,3)
#cell_A1=sheet2.cell(0,0).value
#cell_B2=sheet2.cell(1,1).value
# print (cell_A1)


output=open('data.txt','w',encoding='gbk')
for j in rows:
	# j 是 列表 rows 中的每一个元素
    output.write(' '.join(j))
    # 空格 把j中的每一个元素join起来，输出为string字符串
    output.write('\n')
output.close()
print ("Done")


