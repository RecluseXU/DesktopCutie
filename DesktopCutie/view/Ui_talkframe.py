# -*- coding: utf-8 -*-
'''
Created on 2019年2月18日

@author: RecluseXu
'''

# Form implementation generated from reading ui file 'D:\Python_WorkPlace\pyqt5\learn\cmd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_talkframe(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(701, 437)
        dialog.setSizeGripEnabled(True)
        
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        
        self.show_info_textBrowser = QtWidgets.QTextBrowser(dialog)
        self.show_info_textBrowser.setObjectName("show_info_textBrowser")
        self.gridLayout.addWidget(self.show_info_textBrowser, 0, 0, 1, 1)
        
        self.input_lineEdit = QtWidgets.QLineEdit(dialog)
        self.input_lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.input_lineEdit, 1, 0, 1, 1)
#         self.gridLayout.setRowStretch(0, 3)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    show_info_2 = QtWidgets.QDialog()
    ui = Ui_talkframe()
    ui.setupUi(show_info_2)
    show_info_2.show()
    sys.exit(app.exec_())

