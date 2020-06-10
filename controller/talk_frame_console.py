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



def listen_the_hotkey(after_function):
    '''监听热键，按下则唤醒'''
    from model.hotkey import start_listen_hot_key
    start_listen_hot_key(after_function)