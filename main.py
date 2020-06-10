# -*- coding: utf-8 -*-
'''
Created on 2019年1月26日

@author: RecluseXu
'''
from view.systemTray import SystemTray
from controller.viewConsole import init_creat_view

# 有pyinstall打包无法将动态导入的包导入的缺陷，所以在此处留下原本需要动态导入包
import wxpy

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = SystemTray()
    
    init_creat_view()

    win.show()
    sys.exit(app.exec_())