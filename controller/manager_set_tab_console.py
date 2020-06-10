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

def get_talkframe_hotkey():
    '''获取现在设置的对话框唤醒热键'''
    from model.hotkey import get_hot_key
    return get_hot_key()

def get_talkframe_hotkey_mapper():
    # 得到可用唤醒热键mapper(dict)
    from infoTool.load_Project_Location import get_PressKeyMapper_location
    import json
    loaction = get_PressKeyMapper_location()
    with open(loaction, "r")as f:
        key_mapper = json.load(f)
    return key_mapper

def set_talkframe_hotkey(key1,key2):
    # 设置唤出talkframe的热键
    from model.hotkey import set_hot_key
    return set_hot_key(key1, key2)

def set_talkframe_auto_start(auto_start_boolean):
    '''设置对话窗口自启动'''
    from infoTool.load_manager_set import set_talkframe_auto_start_configure
    set_talkframe_auto_start_configure(auto_start_boolean)

def set_fairyframe_auto_start(auto_start_id):
    '''设置精灵窗口自启动'''
    from infoTool.load_manager_set import set_fairyframe_auto_start_configure
    set_fairyframe_auto_start_configure(auto_start_id)
