# -*- coding: utf-8 -*-

'''
Created on 2019年2月19日

@author: RecluseXu
'''

from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QSize


class Ui_talk_set_tab(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(747, 466)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        
        from controller.talk_set_console import get_icon
        
        self.move_up_pushButton = QtWidgets.QPushButton(Form)
        self.move_up_pushButton.setObjectName("move_up_pushButton")
        self.move_up_pushButton.setEnabled(False)
        self.move_up_pushButton.setIcon(get_icon("arrow_up"))
        self.move_up_pushButton.setFixedSize(48,48)
        self.move_up_pushButton.setIconSize(QSize(40,40))
        self.move_up_pushButton.setToolTip("上移模组")
        self.gridLayout.addWidget(self.move_up_pushButton, 0, 0, 1, 1)
        
        self.move_dowm_pushButton = QtWidgets.QPushButton(Form)
        self.move_dowm_pushButton.setObjectName("move_dowm_pushButton")
        self.move_dowm_pushButton.setEnabled(False)
        self.move_dowm_pushButton.setIcon(get_icon("arrow_down"))
        self.move_dowm_pushButton.setFixedSize(48,48)
        self.move_dowm_pushButton.setIconSize(QSize(40,40))
        self.move_dowm_pushButton.setToolTip("下移模组")
        self.gridLayout.addWidget(self.move_dowm_pushButton, 1, 0, 1, 1)
        
        self.add_pushButton = QtWidgets.QPushButton(Form)
        self.add_pushButton.setObjectName("add_pushButton")
        self.add_pushButton.setIcon(get_icon("add"))
        self.add_pushButton.setFixedSize(48,48)
        self.add_pushButton.setIconSize(QSize(40,40))
        self.add_pushButton.setToolTip("添加模组")
        self.gridLayout.addWidget(self.add_pushButton, 2, 0, 1, 1)
        
        self.delete_pushButton = QtWidgets.QPushButton(Form)
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.delete_pushButton.setEnabled(False)
        self.delete_pushButton.setIcon(get_icon("delete"))
        self.delete_pushButton.setFixedSize(48,48)
        self.delete_pushButton.setIconSize(QSize(40,40))
        self.delete_pushButton.setToolTip("删除模组")
        self.gridLayout.addWidget(self.delete_pushButton, 3, 0, 1, 1)
        
        self.open_judgement_folder_button = QtWidgets.QPushButton(Form)
        self.open_judgement_folder_button.setIcon(get_icon("folder_black"))
        self.open_judgement_folder_button.setFixedSize(48,48)
        self.open_judgement_folder_button.setIconSize(QSize(40,40))
        self.open_judgement_folder_button.setObjectName("open_judgement_folder_button")
        self.open_judgement_folder_button.setToolTip("浏览模组文件夹")
        self.gridLayout.addWidget(self.open_judgement_folder_button, 4, 0, 1, 1)
        
#         self.pushButton_5 = QtWidgets.QPushButton(Form)
#         self.pushButton_5.setObjectName("pushButton_5")
#         self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 1)
        
        self.judge_treeWidget = QtWidgets.QTreeWidget(Form)
        self.judge_treeWidget.setObjectName("treeWidget")
        self.judge_treeWidget.headerItem().setText(0, "名称")
        self.judge_treeWidget.setColumnCount(3)
        self.judge_treeWidget.setColumnWidth(0,200)
        self.judge_treeWidget.setColumnWidth(1,100)
        self.gridLayout.addWidget(self.judge_treeWidget, 0, 1, 7, 1)
        
        self.judge_info_textBrowser = QtWidgets.QTextBrowser(Form)
        self.judge_info_textBrowser.setObjectName("judge_info_textBrowser")
        self.gridLayout.addWidget(self.judge_info_textBrowser, 0, 2, 7, 3)
        
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 3)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
#         self.move_up_pushButton.setText(_translate("Form", "上移"))
#         self.move_dowm_pushButton.setText(_translate("Form", "下移"))
#         self.set_pushButton.setText(_translate("Form", "显示热键设置"))
#         self.open_judgement_folder_button.setText(_translate("Form", "打开判断目录"))
#         self.pushButton_5.setText(_translate("Form", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_talk_set_tab()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())