# -*- coding: utf-8 -*-
'''
Created on 2019年4月10日

@author: RecluseXu
'''
from PyQt5 import QtCore, QtWidgets

class Ui_manager_set_tab(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(747, 466)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        
        
#         #中心控件-中心布局-选项卡控件-设置选项卡-语言选择标签
#         self.setTab_LanguageLabel = QtWidgets.QLabel(Form)
#         self.setTab_LanguageLabel.setObjectName("setTab_LanguageLabel")
#         self.setTab_LanguageLabel.setText("语言：")
#         self.gridLayout.addWidget(self.setTab_LanguageLabel, 0, 0, 1, 1)
#         
#         #中心控件-中心布局-选项卡控件-设置选项卡-语言下拉选框
#         self.setTab_LanguageSelectComboBox = QtWidgets.QComboBox(Form)
#         self.setTab_LanguageSelectComboBox.setObjectName("setTab_LanguageSelectComboBox")
#         self.gridLayout.addWidget(self.setTab_LanguageSelectComboBox, 0, 1, 1, 1)

        #中心控件-中心布局-选项卡控件-设置选项卡-对话框自启动标签
        self.setTab_auto_start_talkframe_Label = QtWidgets.QLabel(Form)
        self.setTab_auto_start_talkframe_Label.setObjectName("setTab_auto_start_talkframe_Label")
        self.setTab_auto_start_talkframe_Label.setText("对话框自启动")
        self.gridLayout.addWidget(self.setTab_auto_start_talkframe_Label, 1, 0, 1, 1)
        
        #中心控件-中心布局-选项卡控件-设置选项卡-对话框自启动多选按钮
        self.auto_start_talkframe_Checkbox = QtWidgets.QCheckBox(Form)
        self.auto_start_talkframe_Checkbox.setObjectName("auto_start_talkframe_checkbox")
        self.gridLayout.addWidget(self.auto_start_talkframe_Checkbox, 1, 1, 1, 1)
        
        #中心控件-中心布局-选项卡控件-设置选项卡-精灵自启动标签
        self.auto_start_fairyframe_Label = QtWidgets.QLabel(Form)
        self.auto_start_fairyframe_Label.setObjectName("auto_start_fairyframe_Label")
        self.auto_start_fairyframe_Label.setText("精灵窗口自启动：")
        self.gridLayout.addWidget(self.auto_start_fairyframe_Label, 2, 0, 1, 1)
        #中心控件-中心布局-选项卡控件-设置选项卡-精灵自启动下拉选框
        self.auto_start_fairyframe_ComboBox = QtWidgets.QComboBox(Form)
        self.auto_start_fairyframe_ComboBox.setObjectName("auto_start_fairyframe_ComboBox")
        self.gridLayout.addWidget(self.auto_start_fairyframe_ComboBox, 2, 1, 1, 1)
        
        #中心控件-中心布局-选项卡控件-设置选项卡-对话窗口唤醒热键标签
        self.set_talkframe_hotkey_Label = QtWidgets.QLabel(Form)
        self.set_talkframe_hotkey_Label.setObjectName("set_talkframe_hotkey_Label")
        self.set_talkframe_hotkey_Label.setText("对话窗口唤醒热键：")
        self.gridLayout.addWidget(self.set_talkframe_hotkey_Label, 3, 0, 1, 1)
         
        #中心控件-中心布局-选项卡控件-设置选项卡-对话窗口唤醒热键下拉选框1
        self.set_talkframe_hotkey1_ComboBox = QtWidgets.QComboBox(Form)
        self.set_talkframe_hotkey1_ComboBox.setObjectName("set_talkframe_hotkey1_ComboBox")
        self.gridLayout.addWidget(self.set_talkframe_hotkey1_ComboBox, 3, 1, 1, 1)
        
        #中心控件-中心布局-选项卡控件-设置选项卡-对话窗口唤醒热键下拉选框2
        self.set_talkframe_hotkey2_ComboBox = QtWidgets.QComboBox(Form)
        self.set_talkframe_hotkey2_ComboBox.setObjectName("set_talkframe_hotkey2_ComboBox")
        self.gridLayout.addWidget(self.set_talkframe_hotkey2_ComboBox, 3, 2, 1, 1)
        
        
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 3)
        self.gridLayout.setColumnStretch(3, 3)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_manager_set_tab()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())