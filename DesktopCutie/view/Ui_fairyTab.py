# -*- coding: utf-8 -*-
'''
Created on 2019年2月9日

@author: RecluseXu
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QFont
from PyQt5.QtCore import Qt

class Ui_FairyTab(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 461)
        Form.setObjectName("FairyTab")
        
        # 精灵选项卡-精灵选项卡布局
        self.fairyTabGridLayout = QtWidgets.QGridLayout(Form)
        self.fairyTabGridLayout.setObjectName("fairyTabGridLayout")
        # 精灵选项卡-精灵选项卡布局-左边的布局
        self.fairyTab_LeftGridLayout = QtWidgets.QGridLayout()
        self.fairyTab_LeftGridLayout.setObjectName("fairyTab_LeftGridLayout")
        # 精灵选项卡-精灵选项卡布局-左边的布局-激活的精灵下拉选框
        self.ActiveFairyComboBox = QtWidgets.QComboBox()
        self.ActiveFairyComboBox.setFrame(True)
        self.ActiveFairyComboBox.setModelColumn(0)
        self.ActiveFairyComboBox.setObjectName("ActiveFairyComboBox")
        self.ActiveFairyComboBox.addItem("已激活的精灵")
        self.fairyTab_LeftGridLayout.addWidget(self.ActiveFairyComboBox, 0, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-左边的布局-添加精灵按钮
        self.addFairyButton = QtWidgets.QPushButton()
        self.addFairyButton.setObjectName("addFairyButton")
        self.fairyTab_LeftGridLayout.addWidget(self.addFairyButton, 0, 1, 1, 1)
        # 精灵选项卡-精灵选项卡布局-左边的布局-用来显示各个资源文件夹的树形控件
        self.treeWidget = QtWidgets.QTreeWidget()
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.fairyTab_LeftGridLayout.addWidget(self.treeWidget, 1, 0, 1, 2)
        # 精灵选项卡-精灵选项卡布局-左边的布局
        self.fairyTab_LeftGridLayout.setColumnStretch(0, 6)
        self.fairyTab_LeftGridLayout.setColumnStretch(1, 2)
        self.fairyTabGridLayout.addLayout(self.fairyTab_LeftGridLayout, 0, 0, 3, 1)
        
        
        # 精灵选项卡-精灵选项卡布局-右边第一层布局
        self.fairyTab_RightFloor1GridLayout = QtWidgets.QGridLayout()
        self.fairyTab_RightFloor1GridLayout.setObjectName("fairyTab_RightFloor1GridLayout")
        # 精灵选项卡-精灵选项卡布局-右边第一层布局-精灵文件名标签
        self.FairyFileNamelabel = QtWidgets.QLabel()
        self.FairyFileNamelabel.setObjectName("FairyFileNamelabel")
        self.FairyFileNamelabel.setFont(QFont("微软雅黑",12,QFont.Bold))
        self.fairyTab_RightFloor1GridLayout.addWidget(self.FairyFileNamelabel, 0, 0, 1, 5)
        # 精灵选项卡-精灵选项卡布局-右边第一层布局-精灵文件夹名标签
        self.FairyFolderNamelabel = QtWidgets.QLabel()
        self.FairyFolderNamelabel.setObjectName("FairyFolderNamelabel")
        self.fairyTab_RightFloor1GridLayout.addWidget(self.FairyFolderNamelabel, 1, 0, 1, 7)
        # 精灵选项卡-精灵选项卡布局-右边第一层布局-卸载按钮
        self.uninstallCutieButton = QtWidgets.QPushButton()
        self.uninstallCutieButton.setObjectName("uninstallCutieButton")  
        self.fairyTab_RightFloor1GridLayout.addWidget(self.uninstallCutieButton, 0, 4, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第一层布局-刷新按钮
        self.reflashOneButton = QtWidgets.QPushButton()
        self.reflashOneButton.setObjectName("reflashOneButton")
        self.fairyTab_RightFloor1GridLayout.addWidget(self.reflashOneButton, 0, 5, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第一层布局-编辑按钮
        self.EditFairyPushButton = QtWidgets.QPushButton()
        self.EditFairyPushButton.setObjectName("EditFairyPushButton")
        self.fairyTab_RightFloor1GridLayout.addWidget(self.EditFairyPushButton, 0, 6, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第一层布局
        self.fairyTabGridLayout.addLayout(self.fairyTab_RightFloor1GridLayout, 0, 1, 1, 1)
        
        # 精灵选项卡-精灵选项卡布局-右边第二层布局
        self.fairyTab_RightFloor2GridLayout = QtWidgets.QGridLayout()
        self.fairyTab_RightFloor2GridLayout.setObjectName("fairyTab_RightFloor2GridLayout")
        # 精灵选项卡-精灵选项卡布局-右边第二层布局-作者名称标签
        self.FairyAuthorLabel = QtWidgets.QLabel()
        self.FairyAuthorLabel.setObjectName("FairyAuthorLabel")
        self.FairyAuthorLabel.setAlignment(Qt.AlignTop)
        self.fairyTab_RightFloor2GridLayout.addWidget(self.FairyAuthorLabel, 0, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第二层布局-精灵版本标签
        self.FairyVersionLabel = QtWidgets.QLabel()
        self.FairyVersionLabel.setObjectName("FairyVersionLabel")
        self.FairyVersionLabel.setAlignment(Qt.AlignTop)
        self.fairyTab_RightFloor2GridLayout.addWidget(self.FairyVersionLabel, 1, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第二层布局-许可标签
        self.FairyLicenseLabel = QtWidgets.QLabel()
        self.FairyLicenseLabel.setObjectName("FairyLicenseLabel")
        self.FairyLicenseLabel.setAlignment(Qt.AlignTop)
        self.FairyLicenseLabel.setWordWrap(True)
        self.fairyTab_RightFloor2GridLayout.addWidget(self.FairyLicenseLabel, 2, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第二层布局-精灵信息标签
        self.FairyInfomationLabel = QtWidgets.QLabel()
        self.FairyInfomationLabel.setObjectName("FairyInfomationLabel")
        self.FairyInfomationLabel.setAlignment(Qt.AlignTop)
        self.FairyInfomationLabel.setWordWrap(True)
        self.fairyTab_RightFloor2GridLayout.addWidget(self.FairyInfomationLabel, 3, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第二层布局
        self.fairyTab_RightFloor2GridLayout.setRowStretch(0, 1)
        self.fairyTab_RightFloor2GridLayout.setRowStretch(1, 1)
        self.fairyTab_RightFloor2GridLayout.setRowStretch(2, 1)
        self.fairyTab_RightFloor2GridLayout.setRowStretch(3, 3)
        self.fairyTabGridLayout.addLayout(self.fairyTab_RightFloor2GridLayout, 1, 1, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局
        self.fairyTab_RightFloor3GridLayout = QtWidgets.QGridLayout()
        self.fairyTab_RightFloor3GridLayout.setObjectName("fairyTab_RightFloor3GridLayout")
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-标签
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.fairyTab_RightFloor3GridLayout.addWidget(self.label, 0, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局
        self.fairyTabGridLayout.addLayout(self.fairyTab_RightFloor3GridLayout, 2, 1, 1, 1)
        # 精灵选项卡-精灵选项卡布局
        self.fairyTabGridLayout.setColumnStretch(0, 2)
        self.fairyTabGridLayout.setColumnStretch(1, 3)
        self.fairyTabGridLayout.setRowStretch(0, 1)
        self.fairyTabGridLayout.setRowStretch(1, 3)
        self.fairyTabGridLayout.setRowStretch(2, 3)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.FairyFileNamelabel.setText(_translate("MainWindow", "设置文件名"))
        self.FairyFolderNamelabel.setText(_translate("MainWindow", "设置目录名"))
        self.uninstallCutieButton.setText(_translate("MainWindow", "卸载"))
        self.reflashOneButton.setText(_translate("MainWindow", "刷新"))
        self.EditFairyPushButton.setText(_translate("MainWindow", "编辑"))
        self.FairyAuthorLabel.setText(_translate("MainWindow", "作者:"))
        self.FairyLicenseLabel.setText(_translate("MainWindow", "许可:"))
        self.FairyInfomationLabel.setText(_translate("MainWindow", "信息:"))
        self.FairyVersionLabel.setText(_translate("MainWindow", "版本:"))
        self.addFairyButton.setText(_translate("MainWindow", "添加"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
#         self.centralWidget_TabWidget.setTabText(self.centralWidget_TabWidget.indexOf(self), _translate("MainWindow", "精灵"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FairyTab()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

