# -*- coding: utf-8 -*-
'''
Created on 2019年2月9日

@author: RecluseXu
'''
from PyQt5 import QtCore,  QtWidgets
from PyQt5.Qt import QFont
from PyQt5.QtCore import Qt
from controller.fairy_tab_console import get_icon

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
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第1行buff第1列
        self.buffer_label = QtWidgets.QLabel()
        self.fairyTab_RightFloor3GridLayout.addWidget(self.buffer_label, 0, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第1行buff第2列—TinyPNG
        self.tinypng_buff_label = QtWidgets.QPushButton()
#         self.tinypng_buff_label = QtWidgets.QLabel()
        self.tinypng_buff_label.setFixedHeight(25)
        self.tinypng_buff_label.setFixedWidth(25)
        self.tinypng_buff_label.setIcon(get_icon("buff_box_black"))
        self.tinypng_buff_label.setCheckable(False)
#         self.tinypng_buff_label.setPixmap(get_icon("buff_box").pixmap(25,25))
        self.fairyTab_RightFloor3GridLayout.addWidget(self.tinypng_buff_label, 0, 1, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第1行buff第2列—添加buff按钮
#         self.add_buff_button = QtWidgets.QPushButton()
#         self.add_buff_button.setFixedWidth(50)
#         self.fairyTab_RightFloor3GridLayout.addWidget(self.add_buff_button, 0, 5, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第2行第1列—动画注册标签
        self.animation_register_set_label = QtWidgets.QLabel()
        self.animation_register_set_label.setObjectName("animation_registe_set_label")
        self.fairyTab_RightFloor3GridLayout.addWidget(self.animation_register_set_label, 1, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第2行第2列—动画注册id下拉菜单
        self.animation_register_combobox = QtWidgets.QComboBox()
        self.animation_register_combobox.setObjectName("animation_register_combobox")
        self.fairyTab_RightFloor3GridLayout.addWidget(self.animation_register_combobox, 1, 1, 1, 5)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第3行第1列—动画逻辑标签
        self.animation_logic_set_label = QtWidgets.QLabel()
        self.animation_logic_set_label.setObjectName("animation_logic_set_label")
        self.fairyTab_RightFloor3GridLayout.addWidget(self.animation_logic_set_label, 2, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第3行第2列—动画逻辑下拉菜单
        self.animation_logic_combobox = QtWidgets.QComboBox()
        self.animation_logic_combobox.setObjectName("animation_logic_combobox")
        self.fairyTab_RightFloor3GridLayout.addWidget(self.animation_logic_combobox, 2, 1, 1, 5)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第4行第1列—动画资源标签
        self.animation_resource_label = QtWidgets.QLabel()
        self.animation_resource_label.setObjectName("animation_resource_label")
        self.fairyTab_RightFloor3GridLayout.addWidget(self.animation_resource_label, 3, 0, 1, 1)
        # 精灵选项卡-精灵选项卡布局-右边第三层布局-第4行第2列—动画资源id下拉菜单
        self.animation_resource_combobox = QtWidgets.QComboBox()
        self.animation_resource_combobox.setObjectName("animation_resource_combobox")
        self.fairyTab_RightFloor3GridLayout.addWidget(self.animation_resource_combobox, 3, 1, 1, 5)
        
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
        self.buffer_label.setText("状态:")
#         self.add_buff_button.setText("添加")
        self.animation_register_set_label.setText(_translate("MainWindow", "注册动画:"))
        self.animation_logic_set_label.setText("动画逻辑:")
        self.animation_resource_label.setText("动画资源:")
#         self.centralWidget_TabWidget.setTabText(self.centralWidget_TabWidget.indexOf(self), _translate("MainWindow", "精灵"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FairyTab()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

