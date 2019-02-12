# -*- coding: utf-8 -*-
'''
Created on 2019年1月26日

@author: RecluseXu
'''
from view.systemTray import SystemTray

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = SystemTray()
    
    win.show()
    sys.exit(app.exec_())