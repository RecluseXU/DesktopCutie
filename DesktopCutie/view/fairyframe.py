# -*- coding: utf-8 -*-
'''
Created on 2019年1月7日

@author: RecluseXu
'''
import time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.Qt import QPoint
from view.Ui_fairyframe import Ui_FairyWindow
from controller import fairy_frame_console



class FairyWindow(QDialog, Ui_FairyWindow):
    def __init__(self, parent=None, fairyID=None):
        super(FairyWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.loadData(fairyID)
        self.initAndStartAnimationTimer()
        self.isHangingAnimation=False
    
    def loadData(self, fairyID):
        # 读取必要的数据，比如动画与窗口信息
        
        # 读取fairy信息
        self.fairy = fairy_frame_console.get_FairyInfo(fairyID)
        
        # 加载动画
        self.animationConsole = fairy_frame_console.load_animation_from_xml(self.fairy.id)
        
        #设置初始窗口位置
        init_location = self.fairy.initWindowLocation
        self.move(int(init_location[0]), int(init_location[1]))
        
        
        
    def initAndStartAnimationTimer(self):
        # 初始化、启动动画计时器
        self.timer = QTimer(self)# 初始化计时器
        self.timer.timeout.connect(self.timer_operation)# 关联事件
        self.timer.start(30)# 设事件间隔，并启动
#         self.timer.setSingleShot(True)
    
    def timer_operation(self):
        #动画计时器操作
#         print(self.animationConsole.nowAnimation.ID,self.animationConsole.nowAnimation.nowImageNumber)
        #检查窗口限制
        windowY = self.geometry().y()
        if(windowY >= self.fairy.windowLocationLimited_Y[1]):
            self.animationConsole.situation.setSituationOntheGround_Yes()
        else:
            self.animationConsole.situation.setSituationOntheGround_No()
        
        #获取动画源
        img, now_resource = self.animationConsole.get_next_resource()

        #更新动画
        self.label.setPixmap(QPixmap.fromImage(img))
        
        
        #Label图像移动
        if(self.animationConsole.situation.isMirrorImage() == True): #镜像图像启动时
            moveX, moveY = now_resource.get("镜像图像偏移")
        else: # 镜像图像未启动时
            moveX, moveY = now_resource.get("图像偏移")
        
        self.label.move(self.retain_space_point.x()+moveX, self.retain_space_point.y()+moveY)
#         self.label.move(100+moveX, 100+moveY)
        
        #窗口移动
        if(now_resource.get("窗口偏移") != [0,0]):
            moveX, moveY = now_resource.get("窗口偏移")
            #移动窗口
            windowX = self.geometry().x()
            if(moveX!=0 and windowX < self.fairy.windowLocationLimited_X[1]):
                windowX = windowX + moveX
            if(moveY!=0 and windowY < self.fairy.windowLocationLimited_Y[1]):
                windowY = windowY + moveY
            self.move(windowX, windowY)
        
        
        #时延
        sleep_time = now_resource.get("时延")
#         self.timer.start(int(sleep_time*2000))
        if(sleep_time != 0):
            time.sleep(sleep_time)
    #--------------------------------------------------
#     def enterEvent(self, event):
#         #鼠标移入事件
# #         self.mouseOnTheLabel = True
#         self.animationConsole.changeAnimationByID("出场空中落下")
#         event.accept()
#         print("")
    #-------------------------------------------------
    
    
    def mousePressEvent(self, event):
        # 鼠标点下去事件
        clicked_Button = event.button()
        event.accept()
        
        # 没有设置点击事件
        if(self.animationConsole.mouse_animation.mouse_click_animation_list is None):
            return
        for click_note in self.animationConsole.mouse_animation.mouse_click_animation_list:
            # 条件都要满足，否则跳过
            if(clicked_Button != click_note["键位"]):
                continue
            if(click_note.get("当前动画id") is not None and click_note["当前动画id"] != self.animationConsole.animation_player.now_register.animation_id):
                continue
            if(click_note.get("发生条件") is not None and fairy_frame_console.check_condition_list(click_note["发生条件"]) == False):
                continue
            # 变更动画
            self.animationConsole.changeAnimationByID(click_note["目标动画"])
            
            if(click_note.get("悬挂点") is not None):
                self.isHangingAnimation=True
                m_Position = event.windowPos().toPoint() #获取鼠标相对窗口的位置
                self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
                #计算挂点到鼠标位置的差值 
                hangPoint = click_note["悬挂点"]
                move = m_Position - self.retain_space_point - hangPoint
#                 move = m_Position - QPoint(100,100) - hangPoint
                new = QPoint(self.geometry().x(),self.geometry().y())
                
                self.move(new + move) #将挂点位置移动到鼠标处
                self.m_Position = self.retain_space_point + hangPoint
#                 self.m_Position = QPoint(100,100) + hangPoint #重置鼠标相对窗口的位置
            if(click_note.get("取消悬挂") is not None):
                self.isHangingAnimation = False
                self.setCursor(QCursor(Qt.ArrowCursor))
                                 
        
    def mouseMoveEvent(self, QMouseEvent):
        # 鼠标移动事件
        if(self.isHangingAnimation and Qt.LeftButton):  
            #QMouseEvent.globalPos() 对于整个显示器来说鼠标的坐标
            #self.m_Position 对窗口来说鼠标的坐标
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
        QMouseEvent.accept()
        
    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放事件
        release_button = QMouseEvent.button()
#         QMouseEvent.accept()
        if(self.animationConsole.mouse_animation.mouse_release_animation_list is None):
            return
        for release_note in self.animationConsole.mouse_animation.mouse_release_animation_list:
            if(release_button != release_note["键位"]):
                continue
            if(release_note.get("当前动画id") is not None and release_note["当前动画id"] != self.animationConsole.animation_player.now_register.animation_id):
                continue
            if(release_note.get("发生条件") is not None and fairy_frame_console.check_condition_list(release_note["发生条件"]) == False):
                continue
            self.animationConsole.changeAnimationByID(release_note["目标动画"])
            if(release_note.get("取消悬挂") is not None):
                self.isHangingAnimation = False
                self.setCursor(QCursor(Qt.ArrowCursor))
        
                            
    def wheelEvent(self, event):
        # 鼠标滚轮事件
        mouse_move_y = event.angleDelta().y()
        if(self.animationConsole.mouse_animation.mouse_wheel_animation_list is None):
            return
        
        for wheel_note in self.animationConsole.mouse_animation.mouse_wheel_animation_list:
            if(wheel_note["滚轮操作"]=="向上" and  mouse_move_y<=0):
                continue
            if(wheel_note["滚轮操作"]=="向下" and  mouse_move_y>=0):
                continue
            if(wheel_note["当前动画id"] is not None and wheel_note["当前动画id"] != self.animationConsole.animation_player.now_register.animation_id):
                continue
            if(wheel_note["发生条件"] is not None and fairy_frame_console.check_condition_list(wheel_note["发生条件"]) == False):
                continue
            self.animationConsole.changeAnimationByID(wheel_note["目标动画"])
        

    
    
    
    def signal_target_to_change_animation(self, operation_name):
        '''
        信号响应
        '''
        print("signal:",operation_name)
        
        self.animationConsole.change_Aniamtion_by_signal(operation_name)
    
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = FairyWindow(fairyID="vat")
    
    win.show()
    sys.exit(app.exec_())
