# -*- coding: utf-8 -*-
'''
Created on 2019年4月10日

@author: RecluseXu
'''

def load_auto_start_info():
    '''读取自启动设置'''
    from infoTool.load_manager_set import get_manager_auto_start_configure
    return get_manager_auto_start_configure()

def get_fairy_id_list():
    '''获取精灵id信息列表'''
    from infoTool.load_Fairy_From_XML_File import scan_FairyXML
    return list(scan_FairyXML().keys())

def set_talkframe_auto_start(auto_start_boolean):
    '''设置对话窗口自启动'''
    from infoTool.load_manager_set import set_talkframe_auto_start_configure
    set_talkframe_auto_start_configure(auto_start_boolean)

def set_fairyframe_auto_start(auto_start_id):
    '''设置精灵窗口自启动'''
    from infoTool.load_manager_set import set_fairyframe_auto_start_configure
    set_fairyframe_auto_start_configure(auto_start_id)