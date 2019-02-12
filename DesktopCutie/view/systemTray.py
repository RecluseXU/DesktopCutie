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
        self.centralWidget.activated.connect(self.trayActivatedEvent)
        self.exit_Action.triggered.connect(self.close_system_tray)
    
    def close_system_tray(self):
        self.quit()
        
    def trayActivatedEvent(self,ActivationReason):
        if(ActivationReason == self.Trigger):
            print("单击")
        elif(ActivationReason == self.DoubleClick):
            print("双击")
            from controller.viewConsole import creat_manager_window
            creat_manager_window()
        elif(ActivationReason == self.MiddleClick):
            print("中键点击")
        

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = SystemTray()
    
    win.show()
    sys.exit(app.exec_())