# -*- coding: utf-8 -*-

"""
Module implementing button_even.
"""

# from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QApplication
from view.Ui_managerframe import Ui_ManagerWindow

class ManagerWindow(QDialog, Ui_ManagerWindow):
    fairyFrameDict={}
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ManagerWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.refreshAllButton.clicked.connect(self.click_RefreshAllButton)
        self.closeButton.clicked.connect(self.click_closeButton)
    
    def close(self, *args, **kwargs):
        from controller.viewConsole import close_manager_window
        close_manager_window()
        return
        
    def click_RefreshAllButton(self):
    #点击刷新全部按钮所执行的函数
        from controller.viewConsole import refresh_all_fairy_frame
        refresh_all_fairy_frame()
        
    def click_closeButton(self):
        from controller.viewConsole import close_manager_window
        close_manager_window()
        
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = ManagerWindow()

    win.show()
    sys.exit(app.exec_())
