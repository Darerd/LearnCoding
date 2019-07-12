# -*- coding: utf-8 -*-

####廖学峰教学Python#####
#####脚本列表####

###1. List 学习##########
L = [
    ['apple','googlr','microsoft'],
    ['java','python','ruby','php'],
    ['adam','bart','lisa']
    ]
print (L[0][0])
print(L[0][-3])
print(L[1][1])
print(L[2][2])
    
###2. if 条件语句#####
height=1.75
weight=80.5
bmi=weight/(height*height)
if bmi < 18.5:
    print('过轻')
elif bmi<=25:
    print('正常')
elif bmi<=28:
    print('过重')
elif bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')
    
    
