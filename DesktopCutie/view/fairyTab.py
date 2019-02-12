# -*- coding: utf-8 -*-
'''
Created on 2019年2月9日

@author: RecluseXu
'''
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QTreeWidgetItem, QIcon
from infoTool.load_Fairy_From_XML_File import scan_FairyXML,get_FairyInfo
from infoTool.load_Project_Location import get_resourceLocation
from view.Ui_fairyTab import Ui_FairyTab

class FairyTab(QWidget, Ui_FairyTab):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(FairyTab, self).__init__(parent)
        self.setupUi(self)
        self.loadingFairyData()
        self.defaultUi()
        
        self.uninstallCutieButton.clicked.connect(self.click_UninstallButton_Function)
        self.ActiveFairyComboBox.activated.connect(self.click_ActiveFairyComboboxItem)
        self.EditFairyPushButton.clicked.connect(self.click_EditFairyPushButton)
        self.reflashOneButton.clicked.connect(self.click_ReflashOneButton)
    
    def click_ReflashOneButton(self):
    #点击刷新（单个）按钮
        fairyID = self.FairyFileNamelabel.text()
        from controller.viewConsole import refresh_a_fairy_frame
        refresh_a_fairy_frame(fairyID)
        
    def click_EditFairyPushButton(self):
    #点击编辑按钮所执行的函数
        fairyID = self.FairyFileNamelabel.text()
        fairy = get_FairyInfo(fairyID)
        from controller.system_shell_console import open
        open(fairy.fairySetXMLLocation)
        print(fairy.fairySetXMLLocation)
    
    def click_UninstallButton_Function(self):
    #当点击 加载（卸载）按钮所执行的函数
        fairyID = self.FairyFileNamelabel.text()
        if(self.uninstallCutieButton.text()=="加载"):
            from controller.viewConsole import creat_a_fairy_frame
            creat_a_fairy_frame(fairyID)
            self.uninstallCutieButton.setText("卸载")
            self.reflashOneButton.setEnabled(True)
        elif(self.uninstallCutieButton.text()=="卸载"):
            from controller.viewConsole import close_a_fairy_frame
            close_a_fairy_frame(fairyID)
            self.uninstallCutieButton.setText("加载")
        self.reflashActiveFairyComboBox()

    def click_ActiveFairyComboboxItem(self,i):
    #当点击已激活精灵复选框内容时执行的函数
        
        # 显示点击的精灵的信息
        fairyID = self.ActiveFairyComboBox.currentText()
        if(fairyID =="已激活的精灵"):
            self.defaultUi()
        else:
            self.fairyInfoShow(fairyID)
            
        # 已激活精灵复选框选项刷新
        self.reflashActiveFairyComboBox()
        
        # 选中并展开TreeWidget对应项
        from PyQt5.QtWidgets import QTreeWidgetItemIterator
        item = QTreeWidgetItemIterator(self.treeWidget)# 获取一个迭代器
        # 利用迭代器遍历TreeWidget,找被选中的精灵，然后在TreeWidget展开、选中
        while(item.value()):
            if(item.value().text(0)==fairyID):
                self.treeWidget.expandItem(item.value())
                item.value().child(0).setSelected(True)
                break
            else:
                item.value().setSelected(False)
            item.__iadd__(1)  # 迭代器位置+1
    
    def reflashActiveFairyComboBox(self):
    #刷新已激活精灵下拉框数据
        self.ActiveFairyComboBox.clear()
        self.ActiveFairyComboBox.addItem("已激活的精灵")
        
        from controller.viewConsole import get_fairy_frame_dict_keys
        active_fairyID_list = get_fairy_frame_dict_keys()
        for fairyid in active_fairyID_list:
            self.ActiveFairyComboBox.addItem(fairyid)
    
    def loadingFairyData(self):
        #读取精灵信息
        folderIcon = QIcon(get_resourceLocation()+"Manager/picture/folder.png")
        fairyDict = scan_FairyXML()
        for fairyID in list(fairyDict.keys()):
            fairy = get_FairyInfo(fairyID)
            child = QTreeWidgetItem(self.treeWidget)
            child.setIcon(0, folderIcon)
            child.setText(0, fairy.id)
            fairyXML = QTreeWidgetItem(child)
            fairyXML.setText(0,fairy.name)
        self.treeWidget.clicked.connect(self.onTreeClicked)
        
    def onTreeClicked(self):
        #树点击事件
        item = self.treeWidget.currentItem()#这里我们需要的是FairyID，所以需要拿的是父母节点的文本
        item = item.parent()
        if(item is None):
            self.defaultUi()
            return 
        fairyID = item.text(0)
        self.fairyInfoShow(fairyID)
        
    def fairyInfoShow(self,fairyID):
        # 在界面中显示精灵信息
        fairy = get_FairyInfo(fairyID)
        self.FairyFileNamelabel.setText(fairyID)
        self.FairyFolderNamelabel.setText(fairy.name+"\t"+fairy.fairySetXMLLocation)
        if(fairy.author is not None):
            self.FairyAuthorLabel.setText("作者: "+fairy.author)
        if(fairy.version is not None):
            self.FairyVersionLabel.setText("版本: "+fairy.version)
        if(fairy.license is not None):
            self.FairyLicenseLabel.setText("许可: "+fairy.license)
        if(fairy.fairyINFO is not None):
            self.FairyInfomationLabel.setText("信息: "+fairy.fairyINFO)
            
        from controller.viewConsole import is_fairy_frame_active
        if(is_fairy_frame_active(fairyID)):  # 已激活精灵的页面
            self.uninstallCutieButton.setText("卸载")
            self.uninstallCutieButton.setEnabled(True)
            self.reflashOneButton.setEnabled(True)
            self.EditFairyPushButton.setEnabled(True)   
        else:  # 未激活精灵的页面
            self.uninstallCutieButton.setText("加载")
            self.uninstallCutieButton.setEnabled(True)
            self.reflashOneButton.setEnabled(False)
            self.EditFairyPushButton.setEnabled(True)
        
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
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    win = FairyTab()

    win.show()
    sys.exit(app.exec_())
