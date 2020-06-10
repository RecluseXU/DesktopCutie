# -*- coding: utf-8 -*-
'''
Created on 2019年2月5日

@author: RecluseXu
'''

from PyQt5.QtWidgets import QSystemTrayIcon, QAction
from view.Ui_systemTray import Ui_SystemTray
from controller import system_tray_console
from PyQt5.QtCore import pyqtSignal


class SystemTray(QSystemTrayIcon, Ui_SystemTray):
    def __init__(self, parent=None):
        super(SystemTray, self).__init__(parent)
        self.setupUi(self)
        self.centralWidget.activated.connect(self.trayActivatedEvent)
        
        self.manager_window_action.triggered.connect(self.click_manager_action)
        self.talk_frame_action.triggered.connect(self.click_talk_frame_action)
        self.exit_Action.triggered.connect(self.close_system_tray)
        
    
    def reflash_all_action(self):
        '''
        刷新右键菜单中的所有内容
        '''
        # 刷新图标
        fairy_frame_key_list = list(system_tray_console.get_all_fairy_frame_dict_keys())
        if(len(fairy_frame_key_list)>0): # 精灵图标
            self.fairy_menu.clear()
            self.fairy_menu.setIcon(system_tray_console.get_icon("screen_on"))
            for fairy_id in fairy_frame_key_list:
                a_active_fairy_frame_menu = self.fairy_menu.addMenu(fairy_id)
                
        else:
            self.fairy_menu.setIcon(system_tray_console.get_icon("screen_off"))
            
        if(system_tray_console.is_talk_frame_active()): # 对话窗口图标
            self.talk_frame_action.setIcon(system_tray_console.get_icon("screen_on"))
        else:
            self.talk_frame_action.setIcon(system_tray_console.get_icon("screen_off"))
    
    def click_talk_frame_action(self):
        '''
        点击右键菜单中的<对话面板>执行的函数
        '''
        system_tray_console.to_creat_talk_frame()
        
    def click_manager_action(self):
        '''
        点击右键菜单中的<管理面板>时执行的函数
        '''
        system_tray_console.to_creat_manager_window()
        
    def close_system_tray(self):
        '''
        点击右键菜单中的<对话面板>执行的函数
        '''
        self.quit()
        
    def trayActivatedEvent(self,ActivationReason):
        '''
        对系统托盘图标的鼠标事件
        '''
        if(ActivationReason == self.Context):# 右键点击托盘图标
            self.reflash_all_action()
        elif(ActivationReason == self.DoubleClick): # 左键双击托盘图标
            system_tray_console.to_creat_manager_window()
        
        
        return
    

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = SystemTray()
    
    win.show()
    sys.exit(app.exec_())