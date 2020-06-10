# -*- coding: utf-8 -*-
'''
Created on 2019年4月10日

@author: RecluseXu
'''
# -*- coding: utf-8 -*-
from view.Ui_manager_set_Tab import Ui_manager_set_tab
from controller import manager_set_tab_console
from PyQt5.QtWidgets import QWidget, QApplication, QTreeWidgetItem, QInputDialog,\
    QMessageBox
from PyQt5.QtCore import Qt


class Manager_set_tab(QWidget, Ui_manager_set_tab):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Manager_set_tab, self).__init__(parent)
        self.setupUi(self)
        
        self.reflash_UI()
        
        self.auto_start_talkframe_Checkbox.stateChanged.connect(self.click_auto_start_talkframe_Checkbox)
        self.auto_start_fairyframe_ComboBox.activated.connect(self.click_auto_start_fairyframe_Combobox)
        self.set_talkframe_hotkey1_ComboBox.activated.connect(self.click_talkframe_hotkey_ComboBox)
        self.set_talkframe_hotkey2_ComboBox.activated.connect(self.click_talkframe_hotkey_ComboBox)
        
        print("管理界面设置页加载完毕")
    
    def reflash_UI(self):
        # 读取自启动设置
        auto_start_dict = manager_set_tab_console.load_auto_start_info()
        
        # 对话框自启动设置
        self.auto_start_talkframe_Checkbox.setChecked(auto_start_dict["TalkFrame"])
        
        # 精灵窗口自启动设置----------------------------------
        self.auto_start_fairyframe_ComboBox.clear()
        fairyId_list = manager_set_tab_console.get_fairy_id_list()
        #    第一个添加的就会变成当前选项
        if(auto_start_dict['FairyFrame'] is not None):
            self.auto_start_fairyframe_ComboBox.addItem(auto_start_dict['FairyFrame'])
        else:
            self.auto_start_fairyframe_ComboBox.addItem("无")
        #    添加剩余的项
        for fairyId in fairyId_list:
            if(auto_start_dict['FairyFrame'] is not None and fairyId == auto_start_dict['FairyFrame']):
                continue
            self.auto_start_fairyframe_ComboBox.addItem(fairyId)
        # 当自启动不为"无"，由于列表添加就不会有"无"，需要手动添加
        if(self.auto_start_fairyframe_ComboBox.itemText(0)!="无"):
            self.auto_start_fairyframe_ComboBox.addItem("无")
        #--------------------------------------------------------
        
        # 读取talkframe唤醒快捷键设置
        key1,key2 = manager_set_tab_console.get_talkframe_hotkey()
        hotkey_mapper = manager_set_tab_console.get_talkframe_hotkey_mapper()
        #    添加当前项
        self.set_talkframe_hotkey1_ComboBox.addItem(key1)
        self.set_talkframe_hotkey2_ComboBox.addItem(key2)
        #    添加剩余项
        hotkey_mapper["MOD"].pop(key1)
        for mod_key in list(hotkey_mapper["MOD"].keys()):
            self.set_talkframe_hotkey1_ComboBox.addItem(mod_key)
        hotkey_mapper["VK"].pop(key2)
        for vk_key in list(hotkey_mapper["VK"].keys()):
            self.set_talkframe_hotkey2_ComboBox.addItem(vk_key)
        
        
        
        
    def click_talkframe_hotkey_ComboBox(self):
        '''
        更变talkframe唤出热键
        '''
        key1 = self.set_talkframe_hotkey1_ComboBox.currentText()
        key2 = self.set_talkframe_hotkey2_ComboBox.currentText()
        if(manager_set_tab_console.set_talkframe_hotkey(key1,key2)):
            QMessageBox.information(self,"提示","修改显示对话窗口的快捷键为\t"+key1+"\t+\t"+key2)
        else:
            QMessageBox.warning(self, "警告", "快捷键注册失败！\n系统已经使用了该快捷键组合")
    
    def change_talkframe_hotkey(self):

        press_key_mapper = manager_set_tab_console.get_talkframe_hotkey_mapper()
        
        # 选第一个快捷键
        key1, ok = QInputDialog.getItem(self, "对话窗口设置", "显示对话窗口-显示键位part1", press_key_mapper["MOD"].keys())
        if(not ok):
            return
        # 选第二个快捷键
        key2, ok = QInputDialog.getItem(self, "对话窗口设置", "显示对话窗口-显示键位part2", press_key_mapper["VK"].keys())
        
        # 设置快捷键
        if(manager_set_tab_console.set_talkframe_hotkey(key1,key2)):
            QMessageBox.information(self, "提示","修改显示对话窗口的快捷键为\t"+key1+"+"+key2)
        else:
            QMessageBox.warning(self, "警告", "快捷键注册失败！\n系统已经使用了该快捷键组合")
    
    def click_auto_start_fairyframe_Combobox(self):
        '''自启动精灵窗口下拉菜单被点击'''
        fairy_id = self.auto_start_fairyframe_ComboBox.currentText()
        if(fairy_id == "无"):
            fairy_id=None
        manager_set_tab_console.set_fairyframe_auto_start(fairy_id)
        
    def click_auto_start_talkframe_Checkbox(self):
        '''状态对话框自启动checkbox改变'''
        # 获取状态
        state = self.auto_start_talkframe_Checkbox.isChecked()
        manager_set_tab_console.set_talkframe_auto_start(state)
        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    win = Manager_set_tab()

    win.show()
    sys.exit(app.exec_())