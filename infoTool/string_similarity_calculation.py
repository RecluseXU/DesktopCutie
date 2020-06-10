# -*- coding: utf-8 -*-
'''
Created on 2019年2月12日

@author: RecluseXu
'''
import Levenshtein

def calculate_hamming_distance(str1, str2):
    # 1） Levenshtein.hamming(str1, str2)
    # 计算 汉明距离。 要求str1和str2必须长度一致。是描述两个等长字串之间 对应 位置上 不同 字符的个数。
    a = Levenshtein.hamming(str1, str2)
#     print(a)
    return a

def calculate_edit_distance(str1, str2):
    # 2）Levenshtein.distance(str1, str2)
    # 计算 编辑距离 （也称为Levenshtein距离 ）。
    # 是描述由一个字串转化成另一个字串最少的操作次数，在其中的操作包括 插入 、删除 、替换 。
    a = Levenshtein.distance(str1,str2)
#     print(a)
    return a

def calculate_ratio_proportion(str1, str2):
    # 3）Levenshtein.ratio(str1, str2)
    # 计算莱文斯坦比。计算公式  r = (sum - ldist) / sum
        #其中sum是指str1 和 str2 字串的长度总和，ldist是 类编辑距离。
    # 注意 ：这里的类编辑距离不是2中所说的编辑距离，2)中三种操作中每个操作+1，而在此处，删除、插入依然+1，但是替换+2。
    #这样设计的目的：ratio('a', 'c')，sum=2,按2中计算为（2-1）/2 = 0.5,’a','c'没有重合，显然不合算，但是替换操作+2，就可以解决这个问题。

    a = Levenshtein.ratio(str1, str2)
#     print(a)
    return a


if __name__ == "__main__":
    calculate_hamming_distance("123a", "a123")
    calculate_edit_distance("123a", "a123")
    calculate_ratio_proportion("123a", "a123")