#!/usr/bin/python3
# -*- coding: UTF-8 -*- 

# from __future__ import unicode_literals
from pypinyin import lazy_pinyin

def sort_pinyin(hanzi_list):        
    hanzi_list_pinyin=[]
    hanzi_list_pinyin_alias_dict={}
    for single_str in hanzi_list:
        py_r = lazy_pinyin(single_str)
        # print("整理下")
        single_str_py=''
        for py_list in py_r:
            single_str_py=single_str_py+py_list
        hanzi_list_pinyin.append(single_str_py)
        hanzi_list_pinyin_alias_dict[single_str_py]=single_str
    hanzi_list_pinyin.sort()
    sorted_hanzi_list=[]
    for single_str_py in hanzi_list_pinyin:
        sorted_hanzi_list.append(hanzi_list_pinyin_alias_dict[single_str_py])
    return sorted_hanzi_list

str=['堡垒之夜','我的世界','饥荒','方舟：生存进化']
print(str)
str=sort_pinyin(str)
print(str)
