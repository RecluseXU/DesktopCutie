# -*- coding: utf-8 -*-
'''
Created on 2019年2月5日

@author: RecluseXu
'''
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication


class Ui_SystemTray(object):
    def setupUi(self,QSystemTrayIcon):
        
        self.centralWidget = QSystemTrayIcon
        self.centralWidget.setIcon(QIcon("F:/MyDocument/Desktop/RM-Skin制作/UI龙之谷/crosssleep.png"))
        
        self.menu = QMenu()
        self.menu.setObjectName("menu")
        self.menu3 = QMenu(self.menu)
        self.menu3.setObjectName("menu3")
#         self.setMenuBar(self.menuBar)
        self.action_2 = QAction(self)
        self.action_2.setObjectName("action_2")
        self.action1 = QAction(self)
        self.action1.setObjectName("action1")
        self.action2 = QAction(self)
        self.action2.setObjectName("action2")
        self.action3_1 = QAction(self)
        self.action3_1.setObjectName("action3_1")
        self.action3_2 = QAction(self)
        self.action3_2.setObjectName("action3_2")
        self.menu3.addAction(self.action3_1)
        self.menu3.addAction(self.action3_2)
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addSeparator()
        self.menu.addAction(self.menu3.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
#         self.menuBar.addAction(self.menu.menuAction())
        
        
        self.centralWidget.setContextMenu(self.menu)
        
        self.retranslateUi(QSystemTrayIcon)
    def retranslateUi(self, QSystemTrayIcon):
        _translate = QCoreApplication.translate
        self.menu.setTitle(_translate("Tray", "推出"))
        self.menu3.setTitle(_translate("Tray", "3"))
        self.action_2.setText(_translate("Tray", "退出"))
        self.action1.setText(_translate("Tray", "1"))
        self.action2.setText(_translate("Tray", "2"))
        self.action3_1.setText(_translate("Tray", "3-1"))
        self.action3_2.setText(_translate("Tray", "3-2"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    systemTray = QSystemTrayIcon()
    ui = Ui_SystemTray()
    ui.setupUi(systemTray)
    systemTray.show()
    sys.exit(app.exec_())