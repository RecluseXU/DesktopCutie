# -*- coding: utf-8 -*-
'''
Created on 2019年2月12日

@author: RecluseXu
'''

def open(location):
    '''传入一个位置，打开对应的 文件/文件夹/程序'''
    from infoTool.cmd_helper import system_shell
    system_shell("start "+location)