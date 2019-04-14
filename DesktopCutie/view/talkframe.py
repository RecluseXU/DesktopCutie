# -*- coding: utf-8 -*-

'''
Created on 2019年2月18日

@author: RecluseXu
'''


from PyQt5.QtWidgets import QDialog
from view.Ui_talkframe import Ui_talkframe
from PyQt5.QtCore import Qt, pyqtSignal
from controller import talk_frame_console

class Talkframe(QDialog, Ui_talkframe):
    """
    Class documentation goes here.
    """
    # 定义一个信号 用于参照判断结果，改变精灵动画的动作
    signal_to_change_fairyframe_animation = pyqtSignal(str)
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Talkframe, self).__init__(parent)
        self.setupUi(self)
        self.input_lineEdit.setFocus()
        
        # 当在文本框内输入回车或退出时
        self.input_lineEdit.returnPressed.connect(self.on_lineedit_input_finish)
        
        
        
    def on_lineedit_input_finish(self):
        '''
        当在输入框内输入回车键时执行的函数
        '''
        input_str = self.input_lineEdit.text()
        
        if(len(input_str) == 0):  # 什么也没输入，直接返回
            return
        
        # 将新内容加在旧内容上
        self.add_str_in_textBrowser(input_str)
        # 清理输入框
        self.input_lineEdit.clear()
        
        # 判断处理新输入的东西
        judge_resoult = talk_frame_console.judge_input(input_str)
        
        # 在显示框中显示判断结果
        self.add_str_in_textBrowser(judge_resoult.get_resoult_info())
        
        # 如果结果中有执行函数，那么执行执行函数
        if(judge_resoult.perform is not None):
            judge_resoult.perform()      
            # 如果执行函数有执行结果，那么显示在显示框上
            if(isinstance(judge_resoult.perform_resoult ,str)):
                self.add_str_in_textBrowser(judge_resoult.perform_resoult)
        
        # 尝试改变精灵界面的动画
        self.signal_to_change_fairyframe_animation.emit(judge_resoult.operation_str)
        
    
    def add_str_in_textBrowser(self, add_str):
        '''
        将一段文件添加在textBrowser后面
        '''
        self.show_info_textBrowser.setPlainText(self.show_info_textBrowser.toPlainText()+">>>"+add_str+"\n")
        
    def keyPressEvent(self, event): 
        #这里event.key（）显示的是按键的编码
#         print("按下：" + str(event.key())) 
        # 举例，这里Qt.Key_A注意虽然字母大写，但按键事件对大小写不敏感 
        if(event.key() == Qt.Key_Escape): 
            # 隐藏对话框
            from controller.viewConsole import hide_talk_frame
            hide_talk_frame()
            
            # 设置系统级热键，监听系统键盘输入，检查到输入就显示对话框
            from model.hotkey import start_listen_hot_key
            from controller.viewConsole import unhide_talk_frame
            start_listen_hot_key(unhide_talk_frame)
            self.input_lineEdit.setFocus()
    
    
    def closeEvent(self, close_event):
        '''
        由于关闭直接关闭对话框也会关闭整个程序，所以这里覆写关闭事件。
        参考：https://blog.csdn.net/ljasdf123/article/details/8918264
        '''
        close_event.ignore()
        print(close_event)
        # 隐藏窗口，开始监听窗口
        from controller.viewConsole import hide_talk_frame
        hide_talk_frame()
        
        from model.hotkey import start_listen_hot_key
        from controller.viewConsole import unhide_talk_frame
        start_listen_hot_key(unhide_talk_frame)
        
    def hide_and_listen_key(self):
        from controller.viewConsole import hide_talk_frame
        hide_talk_frame()
        
        from model.hotkey import start_listen_hot_key
        from controller.viewConsole import unhide_talk_frame
        start_listen_hot_key(unhide_talk_frame)
        
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = Talkframe()

    win.show()
    sys.exit(app.exec_())