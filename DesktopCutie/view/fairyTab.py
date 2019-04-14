# -*- coding: utf-8 -*-
'''
Created on 2019年2月9日

@author: RecluseXu
'''
from PyQt5.QtWidgets import QWidget, QFileDialog, QTreeWidgetItemIterator,\
    QMessageBox
from PyQt5.Qt import QTreeWidgetItem
from view.Ui_fairyTab import Ui_FairyTab
from controller import fairy_tab_console



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
        self.show_fairy_data_in_treewidget() # 刷新树
        self.reflashActiveFairyComboBox() # 刷新已激活精灵下拉框
        self.defaultUi()
        
        self.uninstallCutieButton.clicked.connect(self.click_UninstallButton_Function)
        self.ActiveFairyComboBox.activated.connect(self.click_ActiveFairyComboboxItem)
        self.EditFairyPushButton.clicked.connect(self.click_EditFairyPushButton)
        self.reflashOneButton.clicked.connect(self.click_ReflashOneButton)
        self.treeWidget.clicked.connect(self.onTreeClicked)
        self.addFairyButton.clicked.connect(self.click_addFairyButton)
        
        self.tinypng_buff_label.clicked.connect(self.click_tinypng_buffer)
        print("精灵设置页加载完毕")
        
    def click_tinypng_buffer(self):
        '''
        点击tinyPNG buff图标
        '''
        print("使用tinyPNG压缩所有资源图片")
        fairy_id = self.FairyFileNamelabel.text()
        if(fairy_id == "..."):
            return
        
        reply = QMessageBox.information(self, "TinyPNG压缩图片询问", "是否需要使用TinyPNG压缩精灵资源中所有的图片?\n（此操作用时较多，会造成程序卡住很久很久1张图大概4s时间处理，操作完毕后能永久大大减少图片大小，不会对损坏图片质量，重复压缩无效）", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if(reply == QMessageBox.No):
            return
        #！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        # 有待优化
        #！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！ 
        
        # 获取所有图片资源的的位置list
        all_picture_list = []
        
        from infoTool.load_Fairy_From_XML_File import get_FairyInfo 
        import xml.etree.cElementTree as ET
        from infoTool.load_Project_Location import get_TheCuiteFolderLocation
        xml_add = get_FairyInfo(fairy_id).resourceLocation
        tree = ET.parse(xml_add) 
        root = tree.getroot()   # 获取根节点
        
        for resource_set in root.find("动作资源"):
            resource_set_location = get_TheCuiteFolderLocation(fairy_id) + resource_set.attrib.get("资源地址")
            for picture_node in resource_set:
                picture_file_name = picture_node.get("图像")
                picture_location = resource_set_location+picture_file_name # 计算资源路径
                all_picture_list.append(picture_location)
        
        from model import TinyPNG
        TinyPNG.compressing_image_overwirte_source_file_list(all_picture_list)
        TinyPNG.add_compressed_id(fairy_id)
        self.tinypng_buff_label.setIcon(fairy_tab_console.get_icon("buff_box"))
    
    def click_addFairyButton(self):
        '''
        点击添加按钮
        '''
        file_location = QFileDialog.getOpenFileName(self, '添加精灵', fairy_tab_console.get_resource_location(), 'xml files (*.xml)')[0]
#         print(file_location)
        if(len(file_location)>0):
            fairy_tab_console.copy_fairy_xml_to_resource_folder(file_location)
            self.show_fairy_data_in_treewidget(reScan=True)
            
    def click_ReflashOneButton(self):
    #点击刷新（单个）按钮
        fairyID = self.FairyFileNamelabel.text()
        fairy_tab_console.refresh_fairy_frame(fairyID)
        
    def click_EditFairyPushButton(self):
    #点击编辑按钮所执行的函数
        fairyID = self.FairyFileNamelabel.text()
        fairy = fairy_tab_console.get_fairy_info(fairyID)
        fairy_tab_console.open_xml(fairy.fairySetXMLLocation)
    
    def click_UninstallButton_Function(self):
    #当点击 加载（卸载）按钮所执行的函数
        fairyID = self.FairyFileNamelabel.text()
        if(self.uninstallCutieButton.text()=="加载"):
            fairy_tab_console.creat_fairy_frame(fairyID)
            self.uninstallCutieButton.setText("卸载")
            self.reflashOneButton.setEnabled(True)
        elif(self.uninstallCutieButton.text()=="卸载"):
            fairy_tab_console.close_fairy_frame(fairyID)
            self.uninstallCutieButton.setText("加载")
            self.reflashOneButton.setEnabled(False)
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
        
        active_fairyID_list = fairy_tab_console.get_active_fairy_frame_list()
        
        for fairyid in active_fairyID_list:
            self.ActiveFairyComboBox.addItem(fairyid)
    
    def show_fairy_data_in_treewidget(self, reScan=False):
        #读取精灵信息显示在treeWidget中
        folderIcon = fairy_tab_console.get_icon("folder")
        fairyDict = fairy_tab_console.get_fairy_dict(reScan)
        
#         print(fairyDict)
        self.treeWidget.clear()
#         print("clear")
#         print(list(fairyDict.keys()))
        
        fairy_id_list = list(fairyDict.keys())
        for fairyID in fairy_id_list:
            fairy = fairy_tab_console.get_fairy_info(fairyID)
            
            child = QTreeWidgetItem(self.treeWidget)
            child.setIcon(0, folderIcon)
            
            if(fairy is None):
                child.setText(0, fairyID+"\t这似乎不是注册文件")
                continue
            
            child.setText(0, fairy.id)
            fairyXML = QTreeWidgetItem(child)
            fairyXML.setText(0,fairy.name)
        
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
        fairy = fairy_tab_console.get_fairy_info(fairyID)
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
        
        
        # 状态内容
        from model.TinyPNG import is_id_had_compressed
        #tinyPNG
        if(is_id_had_compressed(fairyID)):
            self.tinypng_buff_label.setIcon(fairy_tab_console.get_icon("buff_box"))
            self.tinypng_buff_label.setCheckable(False)
        else:
            self.tinypng_buff_label.setIcon(fairy_tab_console.get_icon("buff_box_black"))
            self.tinypng_buff_label.setCheckable(True)
            
        # 关于动画信息的内容
        self.animation_register_combobox.clear()
        self.animation_logic_combobox.clear()
        self.animation_resource_combobox.clear()
        
        general_info = fairy_tab_console.get_general_animation_info(fairyID)
        if(general_info is not None):
            self.animation_register_combobox.addItem("一共 "+str(len(general_info.get("注册信息")))+" 条动画信息")
            for register_id in general_info.get("注册信息"):
                self.animation_register_combobox.addItem(register_id)
                
            self.animation_logic_combobox.addItem("一共 "+str(len(general_info.get("逻辑信息")))+" 条逻辑信息")
            for logic_id in general_info.get("逻辑信息"):
                self.animation_logic_combobox.addItem(logic_id)
                
            self.animation_resource_combobox.addItem("一共 "+str(len(general_info.get("资源信息")))+" 条资源信息")
            for resource_id in general_info.get("资源信息"):
                self.animation_resource_combobox.addItem(resource_id)
        
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
        
        self.tinypng_buff_label.setIcon(fairy_tab_console.get_icon("buff_box_black"))
        self.tinypng_buff_label.setCheckable(False)
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    win = FairyTab()

    win.show()
    sys.exit(app.exec_())
