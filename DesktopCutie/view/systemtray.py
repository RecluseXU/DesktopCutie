# -*- coding: utf-8 -*-
'''
Created on 2019年2月5日

@author: RecluseXu
'''
from PyQt5.QtWidgets import QSystemTrayIcon
from view.Ui_systemTray import Ui_SystemTray

class SystemTray(QSystemTrayIcon, Ui_SystemTray):
    def __init__(self, parent=None):
        super(SystemTray, self).__init__(parent)
        self.setupUi(self)
        

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = SystemTray()
    
    win.show()
    sys.exit(app.exec_())