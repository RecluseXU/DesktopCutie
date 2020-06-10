# -*- coding: utf-8 -*-
'''
Created on 2019年2月5日

@author: RecluseXu
'''
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from controller import system_tray_console


class Ui_SystemTray(object):
    def setupUi(self,QSystemTrayIcon):
        
        self.centralWidget = QSystemTrayIcon
        self.centralWidget.setIcon(system_tray_console.get_icon("SystemTray"))
        
        self.menu = QMenu()
        self.menu.setObjectName("menu")
        
        self.exit_Action = QAction(self)
        self.exit_Action.setObjectName("exit_Action")
        
        self.manager_window_action = QAction(self)
        self.manager_window_action.setObjectName("manager_window_action")
        
        self.talk_frame_action = QAction(self)
        self.talk_frame_action.setObjectName("talk_frame_action")
        
        self.fairy_menu = QMenu(self.menu)
        self.fairy_menu.setObjectName("fairy_menu")
        
        self.menu.addAction(self.manager_window_action)
        self.menu.addSeparator()
        self.menu.addAction(self.talk_frame_action)
        self.menu.addAction(self.fairy_menu.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.exit_Action)
#         self.menuBar.addAction(self.menu.menuAction())
        
        
        self.centralWidget.setContextMenu(self.menu)
        
        self.retranslateUi(QSystemTrayIcon)
    
    
    
    def retranslateUi(self, QSystemTrayIcon):
        _translate = QCoreApplication.translate
        self.menu.setTitle(_translate("Tray", "推出"))
        self.fairy_menu.setTitle(_translate("Tray", "精灵"))
        self.exit_Action.setText(_translate("Tray", "退出"))
        self.manager_window_action.setText(_translate("Tray", "管理面板"))
        self.talk_frame_action.setText(_translate("Tray", "对话面板"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    systemTray = QSystemTrayIcon()
    ui = Ui_SystemTray()
    ui.setupUi(systemTray)
    systemTray.show()
    sys.exit(app.exec_())