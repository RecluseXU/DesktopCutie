# -*- coding: utf-8 -*-
'''
Created on 2019年3月9日

@author: RecluseXu
'''


def open_xml(xml_location):
    '''
    用系统软件打开精灵设置xml文件
    '''
    from controller.system_shell_console import open_or_run
    open_or_run({"softwareLocation":xml_location})

def refresh_fairy_frame(fairyID):
    '''
    刷新一个精灵窗口
    '''
    from controller.viewConsole import refresh_a_fairy_frame
    refresh_a_fairy_frame(fairyID)

def copy_fairy_xml_to_resource_folder(file_location):
    '''
    复制精灵设置文件（xml）到资源文件夹
    '''
    from controller.system_shell_console import copy_file_to_resource
    copy_file_to_resource(file_location)

def get_active_fairy_frame_list():
    '''
    获取已经激活的精灵窗口列表
    '''
    from controller.viewConsole import get_fairy_frame_dict_keys
    return get_fairy_frame_dict_keys()

def get_resource_location():
    '''
    获取资源路径
    '''
    from infoTool.load_Project_Location import get_resourceLocation
    return get_resourceLocation()

def creat_fairy_frame(fairyID):
    '''
    创建一个精灵窗口
    '''
    from controller.viewConsole import creat_a_fairy_frame
    creat_a_fairy_frame(fairyID)

def close_fairy_frame(fairyID):
    '''
    关闭一个精灵窗口
    '''
    from controller.viewConsole import close_a_fairy_frame
    close_a_fairy_frame(fairyID)

def get_general_animation_info(fairyID):
    '''获取精灵动画概要信息'''
    from infoTool.fairy_animation_general_info_helper import get_animation_general_info
    return get_animation_general_info(fairyID)

def get_icon(icon_name):
    '''
    获取一个图标(QIcon)
    '''
    from infoTool.load_icon import get_icon_by_key
    return get_icon_by_key(icon_name)

def get_fairy_dict(reScan):
    '''
    获取精灵列表
    传入True可以重新扫描资源目录，如果加入了新的精灵，那么说不定能找到新的
    '''
    from infoTool.load_Fairy_From_XML_File import scan_FairyXML
    return scan_FairyXML(reScan)

def get_fairy_info(fairyID):
    '''
    传入精灵id，返回精灵信息（Fairy类实例）
    '''
    from infoTool.load_Fairy_From_XML_File import get_FairyInfo
    return get_FairyInfo(fairyID)