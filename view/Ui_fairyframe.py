# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.Qt import QPoint

class Ui_FairyWindow(object):
    def setupUi(self, QDialog):
        QDialog.setObjectName("FairyWindow")
        QDialog.resize(500, 500)
        
        self.centralWidget = QtWidgets.QWidget(QDialog)
        self.centralWidget.setObjectName("centralWidget")
        
        #显示图片的标签
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.label.resize(500,500)
        self.label.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        
        # 预先保留空间，流出一些空间来显示图片，以免因为图片过大超出窗口而导致图片显示不全
        self.retain_space_point = QPoint(100,100)
        self.label.move(self.retain_space_point) # 各留出100像素位置给图像位移用
        
        
        self.retranslateUi(QDialog)
        
        QtCore.QMetaObject.connectSlotsByName(QDialog)
    
        
        
        
    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setAttribute(Qt.WA_TranslucentBackground, True) # 窗口背景透明
        # Qt.FramelessWindowHint设置无边框,Qt.WindowStaysOnTopHint窗口保持在前端,Qt.ToolTip设为工具提示窗，不在系统任务栏显示
#         QDialog.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint) 
        QDialog.setWindowFlags(Qt.ToolTip | Qt.FramelessWindowHint)
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FairyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
