# coding:utf-8

#保存文件的方法
def write_data(data, name):
	file_name = name
	with open(file_name, 'a', errors='ignore', newline='') as f:
			f_csv = csv.writer(f)
			f_csv.writerows(data)
			
# csv是Excel文件

##写入文件
with open('1.txt','a',encoding='utf-8') as file:
	file.write(dd)
