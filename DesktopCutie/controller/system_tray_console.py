# -*- coding: utf-8 -*-
'''
Created on 2019年3月27日

@author: RecluseXu
'''

def to_creat_talk_frame():
    '''
    创建或显示对话窗口
    '''
    from controller.viewConsole import creat_talk_frame
    creat_talk_frame()

def to_creat_manager_window():
    '''
    创建管理窗口
    '''
    from controller.viewConsole import creat_manager_window
    creat_manager_window()

def get_all_fairy_frame_dict_keys():
    '''
    获取是否有精灵窗口激活，返回bool值
    '''
    from controller.viewConsole import get_fairy_frame_dict_keys
    return get_fairy_frame_dict_keys()

def is_talk_frame_active():
    '''
    获取对话窗口是否在运行，返回bool值
    '''
    from controller.viewConsole import is_talk_frame_active
    return is_talk_frame_active()

def get_icon(key):
    '''
    传入key(str)，获取图标(QIcon)对象
    '''
    from infoTool.load_icon import get_icon_by_key
    return get_icon_by_key(key)

def close_a_fairy_frame_by_id(fairyID):
    '''
    关闭一个精灵窗口
    '''
    from controller.viewConsole import close_a_fairy_frame
    close_a_fairy_frame(fairyID)