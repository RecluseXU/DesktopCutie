# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python_WorkPlace\pyqt5\learn\mainframe.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 509)
        #中心控件
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        #中心控件-中心布局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #中心控件-中心布局-选项卡控件
        self.centralWidget_TabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.centralWidget_TabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget_TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget_TabWidget.setMovable(False)
        self.centralWidget_TabWidget.setObjectName("centralWidget_TabWidget")
        #中心控件-中心布局-选项卡控件-精灵选项卡
        self.tabWidget_FairyTab = QtWidgets.QWidget()
        self.tabWidget_FairyTab.setObjectName("tabWidget_FairyTab")
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局
        self.fairyTabGridLayout = QtWidgets.QGridLayout(self.tabWidget_FairyTab)
        self.fairyTabGridLayout.setObjectName("fairyTabGridLayout")
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-左边的布局
        self.fairyTab_LeftGridLayout = QtWidgets.QGridLayout()
        self.fairyTab_LeftGridLayout.setObjectName("fairyTab_LeftGridLayout")
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-左边的布局-激活的精灵下拉选框
        self.ActiveFairyComboBox = QtWidgets.QComboBox(self.tabWidget_FairyTab)
        self.ActiveFairyComboBox.setFrame(True)
        self.ActiveFairyComboBox.setModelColumn(0)
        self.ActiveFairyComboBox.setObjectName("ActiveFairyComboBox")
        self.ActiveFairyComboBox.addItem("已激活的精灵")
        self.fairyTab_LeftGridLayout.addWidget(self.ActiveFairyComboBox, 0, 0, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-左边的布局-添加精灵按钮
        self.addFairyButton = QtWidgets.QPushButton(self.tabWidget_FairyTab)
        self.addFairyButton.setObjectName("addFairyButton")
        self.fairyTab_LeftGridLayout.addWidget(self.addFairyButton, 0, 1, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-左边的布局-用来显示各个资源文件夹的树形控件
        self.treeWidget = QtWidgets.QTreeWidget(self.tabWidget_FairyTab)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.fairyTab_LeftGridLayout.addWidget(self.treeWidget, 1, 0, 1, 2)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-左边的布局
        self.fairyTab_LeftGridLayout.setColumnStretch(0, 6)
        self.fairyTab_LeftGridLayout.setColumnStretch(1, 2)
        self.fairyTabGridLayout.addLayout(self.fairyTab_LeftGridLayout, 0, 0, 3, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第一层布局
        self.fairyTab_RightFloor1GridLayout = QtWidgets.QGridLayout()
        self.fairyTab_RightFloor1GridLayout.setObjectName("fairyTab_RightFloor1GridLayout")
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第一层布局-精灵文件名标签
        self.FairyFileNamelabel = QtWidgets.QLabel(self.tabWidget_FairyTab)
        self.FairyFileNamelabel.setObjectName("FairyFileNamelabel")
        self.FairyFileNamelabel.setFont(QFont("微软雅黑",12,QFont.Bold))
        self.fairyTab_RightFloor1GridLayout.addWidget(self.FairyFileNamelabel, 0, 0, 1, 5)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第一层布局-精灵文件夹名标签
        self.FairyFolderNamelabel = QtWidgets.QLabel(self.tabWidget_FairyTab)
        self.FairyFolderNamelabel.setObjectName("FairyFolderNamelabel")
        self.fairyTab_RightFloor1GridLayout.addWidget(self.FairyFolderNamelabel, 1, 0, 1, 7)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第一层布局-卸载按钮
        self.uninstallCutieButton = QtWidgets.QPushButton(self.tabWidget_FairyTab)
        self.uninstallCutieButton.setObjectName("uninstallCutieButton")  
        self.fairyTab_RightFloor1GridLayout.addWidget(self.uninstallCutieButton, 0, 4, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第一层布局-刷新按钮
        self.reflashOneButton = QtWidgets.QPushButton(self.tabWidget_FairyTab)
        self.reflashOneButton.setObjectName("reflashOneButton")
        self.fairyTab_RightFloor1GridLayout.addWidget(self.reflashOneButton, 0, 5, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第一层布局-编辑按钮
        self.EditFairyPushButton = QtWidgets.QPushButton(self.tabWidget_FairyTab)
        self.EditFairyPushButton.setObjectName("EditFairyPushButton")
        self.fairyTab_RightFloor1GridLayout.addWidget(self.EditFairyPushButton, 0, 6, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第一层布局
        self.fairyTabGridLayout.addLayout(self.fairyTab_RightFloor1GridLayout, 0, 1, 1, 1)
        
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第二层布局
        self.fairyTab_RightFloor2GridLayout = QtWidgets.QGridLayout()
        self.fairyTab_RightFloor2GridLayout.setObjectName("fairyTab_RightFloor2GridLayout")
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第二层布局-作者名称标签
        self.FairyAuthorLabel = QtWidgets.QLabel(self.tabWidget_FairyTab)
        self.FairyAuthorLabel.setObjectName("FairyAuthorLabel")
        self.FairyAuthorLabel.setAlignment(Qt.AlignTop)
        self.fairyTab_RightFloor2GridLayout.addWidget(self.FairyAuthorLabel, 0, 0, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第二层布局-精灵版本标签
        self.FairyVersionLabel = QtWidgets.QLabel(self.tabWidget_FairyTab)
        self.FairyVersionLabel.setObjectName("FairyVersionLabel")
        self.FairyVersionLabel.setAlignment(Qt.AlignTop)
        self.fairyTab_RightFloor2GridLayout.addWidget(self.FairyVersionLabel, 1, 0, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第二层布局-许可标签
        self.FairyLicenseLabel = QtWidgets.QLabel(self.tabWidget_FairyTab)
        self.FairyLicenseLabel.setObjectName("FairyLicenseLabel")
        self.FairyLicenseLabel.setAlignment(Qt.AlignTop)
        self.FairyLicenseLabel.setWordWrap(True)
        self.fairyTab_RightFloor2GridLayout.addWidget(self.FairyLicenseLabel, 2, 0, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第二层布局-精灵信息标签
        self.FairyInfomationLabel = QtWidgets.QLabel(self.tabWidget_FairyTab)
        self.FairyInfomationLabel.setObjectName("FairyInfomationLabel")
        self.FairyInfomationLabel.setAlignment(Qt.AlignTop)
        self.FairyInfomationLabel.setWordWrap(True)
        self.fairyTab_RightFloor2GridLayout.addWidget(self.FairyInfomationLabel, 3, 0, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第二层布局
        self.fairyTab_RightFloor2GridLayout.setRowStretch(0, 1)
        self.fairyTab_RightFloor2GridLayout.setRowStretch(1, 1)
        self.fairyTab_RightFloor2GridLayout.setRowStretch(2, 1)
        self.fairyTab_RightFloor2GridLayout.setRowStretch(3, 3)
        self.fairyTabGridLayout.addLayout(self.fairyTab_RightFloor2GridLayout, 1, 1, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第三层布局
        self.fairyTab_RightFloor3GridLayout = QtWidgets.QGridLayout()
        self.fairyTab_RightFloor3GridLayout.setObjectName("fairyTab_RightFloor3GridLayout")
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第三层布局-标签
        self.label = QtWidgets.QLabel(self.tabWidget_FairyTab)
        self.label.setObjectName("label")
        self.fairyTab_RightFloor3GridLayout.addWidget(self.label, 0, 0, 1, 1)
        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局-右边第三层布局
        self.fairyTabGridLayout.addLayout(self.fairyTab_RightFloor3GridLayout, 2, 1, 1, 1)

        #中心控件-中心布局-选项卡控件-精灵选项卡-精灵选项卡布局
        self.fairyTabGridLayout.setColumnStretch(0, 2)
        self.fairyTabGridLayout.setColumnStretch(1, 3)
        self.fairyTabGridLayout.setRowStretch(0, 1)
        self.fairyTabGridLayout.setRowStretch(1, 3)
        self.fairyTabGridLayout.setRowStretch(2, 3)
        self.centralWidget_TabWidget.addTab(self.tabWidget_FairyTab, "")
        
        #中心控件-中心布局-选项卡控件-设置选项卡
        self.SetTab = QtWidgets.QWidget()
        self.SetTab.setObjectName("SetTab")
        #中心控件-中心布局-选项卡控件-设置选项卡-语言下拉选框
        self.setTab_LanguageSelectComboBox = QtWidgets.QComboBox(self.SetTab)
        self.setTab_LanguageSelectComboBox.setGeometry(QtCore.QRect(120, 40, 371, 20))
        self.setTab_LanguageSelectComboBox.setObjectName("setTab_LanguageSelectComboBox")
        #中心控件-中心布局-选项卡控件-设置选项卡-语言选择标签
        self.setTab_LanguageLabel = QtWidgets.QLabel(self.SetTab)
        self.setTab_LanguageLabel.setGeometry(QtCore.QRect(54, 40, 48, 16))
        self.setTab_LanguageLabel.setObjectName("setTab_LanguageLabel")
        #中心控件-中心布局-选项卡控件-设置选项卡
        self.centralWidget_TabWidget.addTab(self.SetTab, "")
        #中心控件-中心布局-选项卡控件
        self.verticalLayout.addWidget(self.centralWidget_TabWidget)
        #中心控件-中心布局-下方布局
        self.centralWidget_BelowGridLayout = QtWidgets.QGridLayout()
        self.centralWidget_BelowGridLayout.setObjectName("centralWidget_BelowGridLayout")
        #中心控件-中心布局-下方布局-刷新全部按钮
        self.refreshAllButton = QtWidgets.QPushButton(self.centralWidget)
        self.refreshAllButton.setObjectName("refreshAllButton")
        self.centralWidget_BelowGridLayout.addWidget(self.refreshAllButton, 0, 0, 1, 1)
        #中心控件-中心布局-下方布局-查看日志按钮
        self.watchLogButton = QtWidgets.QPushButton(self.centralWidget)
        self.watchLogButton.setObjectName("watchLogButton")
        self.centralWidget_BelowGridLayout.addWidget(self.watchLogButton, 0, 1, 1, 1)
        #中心控件-中心布局-下方布局-帮助按钮
        self.helpButton = QtWidgets.QPushButton(self.centralWidget)
        self.helpButton.setObjectName("helpButton")
        self.centralWidget_BelowGridLayout.addWidget(self.helpButton, 0, 3, 1, 1)
        #中心控件-中心布局-下方布局-关闭按钮
        self.closeButton = QtWidgets.QPushButton(self.centralWidget)
        self.closeButton.setObjectName("closeButton")
        self.centralWidget_BelowGridLayout.addWidget(self.closeButton, 0, 4, 1, 1)
        #中心控件-中心布局-下方布局
        self.centralWidget_BelowGridLayout.setColumnStretch(0, 1)
        self.centralWidget_BelowGridLayout.setColumnStretch(1, 1)
        self.centralWidget_BelowGridLayout.setColumnStretch(2, 4)
        self.centralWidget_BelowGridLayout.setColumnStretch(3, 1)
        self.centralWidget_BelowGridLayout.setColumnStretch(4, 1)
        self.verticalLayout.addLayout(self.centralWidget_BelowGridLayout)
        #中心控件-中心布局
        MainWindow.setCentralWidget(self.centralWidget)
        
        
        self.retranslateUi(MainWindow)
        self.centralWidget_TabWidget.setCurrentIndex(0)
        
        self.closeButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.centralWidget_TabWidget.setTabText(self.centralWidget_TabWidget.indexOf(self.tabWidget_FairyTab), _translate("MainWindow", "精灵"))
        self.setTab_LanguageLabel.setText(_translate("MainWindow", "Language"))
        self.centralWidget_TabWidget.setTabText(self.centralWidget_TabWidget.indexOf(self.SetTab), _translate("MainWindow", "设置"))
        self.helpButton.setText(_translate("MainWindow", "帮助"))
        self.refreshAllButton.setText(_translate("MainWindow", "刷新全部"))
        self.watchLogButton.setText(_translate("MainWindow", "查看日志"))
        self.closeButton.setText(_translate("MainWindow", "关闭"))
        self.defaultUi()

    def defaultUi(self):
        self.FairyFileNamelabel.setText("...")
        self.FairyFolderNamelabel.setText("")
        self.FairyAuthorLabel.setText("作者:")
        self.FairyInfomationLabel.setText("信息:")
        self.FairyLicenseLabel.setText("许可:")
        self.FairyVersionLabel.setText("版本:")
        self.uninstallCutieButton.setDisabled(True)
        self.reflashOneButton.setDisabled(True)
        self.EditFairyPushButton.setDisabled(True)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

