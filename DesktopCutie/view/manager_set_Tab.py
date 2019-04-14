# -*- coding: utf-8 -*-
'''
Created on 2019年4月10日

@author: RecluseXu
'''
# -*- coding: utf-8 -*-
from view.Ui_manager_set_Tab import Ui_manager_set_tab
'''
Created on 2019年2月19日

@author: RecluseXu
'''

from PyQt5.QtWidgets import QWidget, QApplication, QTreeWidgetItem, QInputDialog,\
    QMessageBox
from PyQt5.QtCore import Qt
from controller import manager_set_tab_console

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
        print("管理界面设置页加载完毕")
    
    def reflash_UI(self):
        # 读取自启动设置
        auto_start_dict = manager_set_tab_console.load_auto_start_info()
        # 对话框自启动设置
        self.auto_start_talkframe_Checkbox.setChecked(auto_start_dict["TalkFrame"])
        # 精灵窗口自启动设置
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