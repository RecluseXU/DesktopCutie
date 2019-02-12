# -*- coding: utf-8 -*-
'''
Created on 2019年2月10日

@author: RecluseXu
'''
from view.systemTray import SystemTray
from view.managerframe import ManagerWindow
from view.fairyframe import FairyWindow

single_manager_window = None
single_system_tray = None
single_fairy_frame_dict = {}


def close_system_tray():
    '''关闭系统托盘'''
    global single_system_tray
    single_system_tray.close()
    single_system_tray = None

def creat_system_tray():
    '''创建系统托盘'''
    global single_system_tray
    if(single_system_tray is None):
        single_system_tray = SystemTray()
        SystemTray.show()
    
def close_manager_window():
    '''关闭管理窗口'''
    global single_manager_window
    single_manager_window.destroy()
    single_manager_window = None
    
def creat_manager_window():
    '''创建管理窗口'''
    global single_manager_window
    if(single_manager_window is None):
        single_manager_window = ManagerWindow()
        single_manager_window.show()

def is_fairy_frame_active(fairyID):
    '''传入精灵ID窗口是否已经激活'''
    for active_fairyID in get_fairy_frame_dict_keys():
        if(active_fairyID == fairyID):
            return True
    return False
    
def get_fairy_frame_dict_keys():
    '''返回已经激活的精灵窗口的 精灵ID 列表'''
    global single_fairy_frame_dict
    return single_fairy_frame_dict.keys()
    
def get_fairy_frame_dict_length():
    '''返回已经激活的精灵窗口数量'''
    global single_fairy_frame_dict
    return len(single_fairy_frame_dict)

def refresh_all_fairy_frame():
    '''刷新所有精灵窗口'''
    global single_fairy_frame_dict
    for fairyID in single_fairy_frame_dict.keys():
        refresh_a_fairy_frame(fairyID)
    
def refresh_a_fairy_frame(fairyID):
    '''刷新一个精灵窗口，实际上就是关了再开'''
    close_a_fairy_frame(fairyID)
    creat_a_fairy_frame(fairyID)
    
def close_a_fairy_frame(fairyID):
    '''销毁一个精灵窗口'''
    global single_fairy_frame_dict
    single_fairy_frame_dict[fairyID].destroy()
    single_fairy_frame_dict[fairyID]=None
    single_fairy_frame_dict.pop(fairyID)
    
def creat_a_fairy_frame(fairyID):
    '''创建一个精灵窗口'''
    global single_fairy_frame_dict
    single_fairy_frame_dict[fairyID] = FairyWindow(fairyID=fairyID)
    single_fairy_frame_dict[fairyID].show()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    tray = SystemTray()
    
    tray.show()
    sys.exit(app.exec_())