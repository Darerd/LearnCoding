with open('data.txt', 'r', encoding='gbk') as rf:
    
    # readline()用于从文件读取整行，包括“\n”字符
    # 如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
    # 参考链接：https://www.runoob.com/python3/python3-file-readline.html
    d = rf.readlines()
    # 输出d 的类型
    #print (type(d))
    # 结果显示为 list
    #print(d)
    # 参考链接：https://blog.csdn.net/weixin_42168614/article/details/88292146
    # 讲解read,readline,readlines的用法
    for i in d:
        dd = i.split(' ')
        output= open('{}.txt'.format(dd[1]), 'w', encoding='gbk')
        dd.pop(1)
        for j in dd:
            output.write(str(j))
    # 空格 把j中的每一个元素join起来，输出为string字符串
            output.write('\n')
        output.close()
    print ("Done")
