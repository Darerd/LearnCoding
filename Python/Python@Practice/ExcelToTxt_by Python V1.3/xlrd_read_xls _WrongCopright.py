### 参考链接：https://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html ####

import xlrd
#import numpy as np


workbook = xlrd.open_workbook(r'C:\Users\yuhui\Desktop\Python读取excel文件内容\1.xls')#打开文件
# print(workbook.sheet_names())#获取所有表格名字
sheet2 = workbook.sheet_by_name('Sheet2') ## 根据sheet名称获取sheet内容

# sheet的名称、行数和列数
#print (sheet2.name,sheet2.nrows,sheet2.ncols)

# 获取行数和列数
nrows= sheet2.nrows
ncols= sheet2.ncols

# 获取整行和整列的值（数组形式）
#rows=sheet2.row_values(3) # 获取第四行内容
#cols=sheet2.col_values(2) # 获取第三列内容
# print (rows,cols)

# 循环行列表数据
for i in range(nrows):
    rows= sheet2.row_values(i)
    print (rows)
    
# 获取单元格的内容
# 第3行4列的cell写法为：cell(2,3)
#cell_A1=sheet2.cell(0,0).value
#cell_B2=sheet2.cell(1,1).value
# print (cell_A1)
output=open('data.txt','w',encoding='gbk')
for j in rows:
    #rowtxt = '{}{}'.format(row[0],row[1])
    output.write(j)
    output.write('\n')
output.close()
print ("Done")


