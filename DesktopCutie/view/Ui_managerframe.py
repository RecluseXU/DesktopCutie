# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python_WorkPlace\pyqt5\learn\mainframe.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from view.fairyTab import FairyTab

class Ui_ManagerWindow(object):
    def setupUi(self, QDialog):
        QDialog.setObjectName("QDialog")
        QDialog.resize(750, 509)
        #中心控件
        self.centralWidget = QDialog
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
        self.FairyTab = FairyTab()
        self.centralWidget_TabWidget.addTab(self.FairyTab, "")
        
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
        
        
        self.retranslateUi(QDialog)
        self.centralWidget_TabWidget.setCurrentIndex(0)
        
        QtCore.QMetaObject.connectSlotsByName(QDialog)

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("QDialog", "QDialog"))
#         self.label.setText(_translate("QDialog", "TextLabel"))
        self.centralWidget_TabWidget.setTabText(self.centralWidget_TabWidget.indexOf(self.FairyTab), _translate("QDialog", "精灵"))
        self.setTab_LanguageLabel.setText(_translate("QDialog", "Language"))
        self.centralWidget_TabWidget.setTabText(self.centralWidget_TabWidget.indexOf(self.SetTab), _translate("QDialog", "设置"))
        self.helpButton.setText(_translate("QDialog", "帮助"))
        self.refreshAllButton.setText(_translate("QDialog", "刷新全部"))
        self.watchLogButton.setText(_translate("QDialog", "查看日志"))
        self.closeButton.setText(_translate("QDialog", "关闭"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QDialog = QtWidgets.QDialog()
    ui = Ui_ManagerWindow()
    ui.setupUi(QDialog)
    QDialog.show()
    sys.exit(app.exec_())

