# -*- coding: utf-8 -*-
'''
Created on 2019年2月19日

@author: RecluseXu
'''

from PyQt5.QtWidgets import QWidget, QApplication, QTreeWidgetItem, QInputDialog,\
    QMessageBox
from PyQt5.QtCore import Qt
from view.Ui_talk_set_Tab import Ui_talk_set_tab
from controller import talk_set_console 
from model.hotkey import set_hot_key



class Talk_set_tab(QWidget, Ui_talk_set_tab):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Talk_set_tab, self).__init__(parent)
        self.setupUi(self)
        self.loading_judgement()
        
        self.judge_info_textBrowser.setText(talk_set_console.get_aim_introduce("defalut"))
        
        self.judge_treeWidget.itemClicked.connect(self.click_treewidget_item)
        self.judge_treeWidget.itemDoubleClicked.connect(self.double_click_treewidget_item)
        self.judge_treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        
        self.move_up_pushButton.clicked.connect(self.click_judge_step_move_up_button)
        self.move_dowm_pushButton.clicked.connect(self.click_judge_step_move_down_button)
        self.set_pushButton.clicked.connect(self.click_set_button)
        self.open_judgement_folder_button.clicked.connect(self.click_open_judgement_folder_button)
        
        
        print("精灵设置页加载完毕")
    
    def click_open_judgement_folder_button(self):
        '''
        点击打开判断模型文件夹按钮
        '''
        talk_set_console.open_judgement_folder()
        
    def click_set_button(self):
        press_key_mapper = talk_set_console.get_press_key_mapper()
        # 选第一个快捷键
        key1, ok = QInputDialog.getItem(self, "对话窗口设置", "显示对话窗口-显示键位part1", press_key_mapper["MOD"].keys())
        if(not ok):
            return
        # 选第二个快捷键
        key2, ok = QInputDialog.getItem(self, "对话窗口设置", "显示对话窗口-显示键位part2", press_key_mapper["VK"].keys())
        
        # 设置快捷键
        if(set_hot_key(key1,key2)):
            QMessageBox.information(self,"提示","修改显示对话窗口的快捷键为\t"+key1+"\t+\t"+key2)
        else:
            QMessageBox.warning(self, "警告", "快捷键注册失败！\n系统已经使用了该快捷键组合")
        
    def click_judge_step_move_down_button(self):
        '''
        点击判断步骤下移按钮
        '''
        current_item = self.judge_treeWidget.currentItem()
        # 是判断步骤的项
        if(len(current_item.text(2)) == 1):
            talk_set_console.judge_step_move_down(current_item.text(0))
            self.loading_judgement()
            self.move_up_pushButton.setEnabled(False)
            self.move_dowm_pushButton.setEnabled(False)
    
    def click_judge_step_move_up_button(self):
        '''
        点击判断步骤上移按钮
        '''
        current_item = self.judge_treeWidget.currentItem()
        # 是判断步骤的项 且 不能是第一个了就没得上移
        if(len(current_item.text(2))==1 and current_item.text(2)!="1"):
            talk_set_console.judge_step_move_up(current_item.text(0))
            self.loading_judgement()
            self.move_up_pushButton.setEnabled(False)
            self.move_dowm_pushButton.setEnabled(False)
            
    
    def loading_judgement(self):
        '''
        读取judge列表的数据,显示在treewidge中
        '''
        self.judge_treeWidget.clear()
        judge_step_list = talk_set_console.get_the_judge_step_list()
        judge_index = 0
        
        for judge in judge_step_list:
            judge_index = judge_index+1
            node = QTreeWidgetItem(self.judge_treeWidget)
            node.setText(0,judge[0])
            node.setText(2,str(judge_index))
            node.setExpanded(True)
            if(judge[1]=="1"):
                node.setCheckState(0, Qt.Checked)
            else:
                node.setCheckState(0, Qt.Unchecked)
                # 当节点未被启用，其子节点直接不显示
#                 continue
            
            # 命令匹配下的子节点添加
            if(judge[0] == "CommandMatching"):
                matching_dict = talk_set_console.get_the_command_matching_mapper()
#                 print(matching_dict)
                matching_index = 0
                
                for match_key in list(matching_dict.keys()):
                    matching_index = matching_index+1
                    sub_node = QTreeWidgetItem(node)
                    sub_node.setText(0,match_key)
                    sub_node.setText(2, str(judge_index) + '-' + str(matching_index))
                    if(matching_dict[match_key][1] == 0):
                        sub_node.setCheckState(0, Qt.Unchecked)
                    else:
                        sub_node.setCheckState(0, Qt.Checked)
                    sub_node.setExpanded(True)
                    
                    sub_sub_node = QTreeWidgetItem(sub_node)
                    sub_sub_node.setText(0, "匹配关键字:")
                    sub_sub_node.setIcon(0,talk_set_console.get_icon("set"))
                    sub_sub_node.setText(1, matching_dict[match_key][0])
                    sub_sub_node.setText(2, str(judge_index) + '-' + str(matching_index) + "-1")
                    
                    if(sub_node.text(0)=="OpenSoftwareOrFolder"): #当序号为1-1即为OpenSoftwareOrFolder
                        sub_sub_node2 = QTreeWidgetItem(sub_node)
                        sub_sub_node2.setText(0, "SoftwareMapper")
                        sub_sub_node2.setText(2, str(judge_index) + '-' + str(matching_index) + "-2")
                        
                        sub_sub_node2.setIcon(0,talk_set_console.get_icon("set"))
                        
                        software_mapper_dict = talk_set_console.get_the_software_mapper()
                        
                        for software in list(software_mapper_dict.keys()):
                            sub_sub_sub_node = QTreeWidgetItem(sub_sub_node2)
                            sub_sub_sub_node.setText(0, software)
                            sub_sub_sub_node.setText(1, software_mapper_dict[software])
                            sub_sub_sub_node.setFlags(Qt.ItemIsEditable)
            
            if(judge[0] == "TuringAI"):
                sub_node = QTreeWidgetItem(node)
                sub_node.setText(0, "信息设置")
                sub_node.setText(2, str(judge_index)+"-1")
                sub_node.setIcon(0, talk_set_console.get_icon("set"))
                
                
    
    def click_treewidget_item(self,clicked_QTreeWidgetItem, clicked_column):
        '''treewidget鼠标单击事件'''
        clicked_text = clicked_QTreeWidgetItem.text(0)
        
        # 显示简介信息
        self.judge_info_textBrowser.setText(talk_set_console.get_aim_introduce(clicked_text))
        
        # 开关选项按钮,点击能启用或禁用判断
        checkstate = clicked_QTreeWidgetItem.checkState(0) # 此处返回的值，选中了返回2，没选中返回0。
        
        # 当这个节点序号长度为1，说明这个节点是判断步骤节点
        if(len(clicked_QTreeWidgetItem.text(2)) == 1):
            # 处理开启与关闭
            if(checkstate == 0):
                talk_set_console.disable_a_judge_step(clicked_text)
            else:
                talk_set_console.enable_a_judge_step(clicked_text)
            # 处理上下移动按钮
            self.move_up_pushButton.setEnabled(True)
            self.move_dowm_pushButton.setEnabled(True)
        else:
            self.move_dowm_pushButton.setEnabled(False)
            self.move_up_pushButton.setEnabled(False)
            
            # 当这个节点父母的是Command_matching的时
            if(clicked_QTreeWidgetItem.parent().text(0) == "CommandMatching"):
                if(checkstate == 0):
                    talk_set_console.disable_a_command_matching(clicked_text)
                else:
                    talk_set_console.enable_a_command_matching(clicked_text)
    
    def double_click_treewidget_item(self,clicked_QTreeWidgetItem, column_int):
        '''treewidget双击事件'''
        # 当双击SoftwareMapper时
        if(clicked_QTreeWidgetItem.text(0)=="SoftwareMapper"):
            talk_set_console.open_software_mapper_file()
            
        elif(clicked_QTreeWidgetItem.text(0) == "匹配关键字:"):
            talk_set_console.open_command_matching_mapper_file()
        
        elif(clicked_QTreeWidgetItem.text(0) == "信息设置"):
            talk_set_console.open_turing_ai_set_file()
    

        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    win = Talk_set_tab()

    win.show()
    sys.exit(app.exec_())