# -*- coding: utf-8 -*-
'''
Created on 2019年3月14日

@author: RecluseXu
'''

def judge_input(input_str):
    '''
    用判断插件来判断输入，得到判断结果
    '''
    from model.judge.judge_console import judge_process
    return judge_process(input_str)

