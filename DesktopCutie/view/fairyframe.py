# -*- coding: utf-8 -*-
'''
Created on 2019年1月7日

@author: RecluseXu
'''
import time

from PyQt5.QtCore import Qt, QTimer

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QCursor,QPixmap
from PyQt5.Qt import QPoint
from view.Ui_fairyframe import Ui_FairyWindow

from infoTool.situation import setSituationOntheGround, isOnTheGround
from infoTool.situation import isMirrorImage


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
        from infoTool.load_Fairy_From_XML_File import get_FairyInfo
        self.fairy = get_FairyInfo(fairyID)
        
        # 加载动画
        from infoTool.load_Animation_from_xml import load_animation_from_xml
        self.animationConsole = load_animation_from_xml(self.fairy.id)
        
        #设置初始窗口位置
        init_location = self.fairy.initWindowLocation
        self.move(int(init_location[0]), int(init_location[1]))
        
        
        
    def initAndStartAnimationTimer(self):
        # 初始化、启动动画计时器
        self.timer = QTimer(self)# 初始化计时器
        self.timer.timeout.connect(self.timer_operation)# 关联事件
        self.timer.start(35)# 设事件间隔，并启动
    
    def timer_operation(self):
        #动画计时器操作
#         print(self.animationConsole.nowAnimation.ID,self.animationConsole.nowAnimation.nowImageNumber)
        #检查窗口限制
        windowY = self.geometry().y()
        if(windowY < self.fairy.windowLocationLimited_Y[1]):
            setSituationOntheGround(False)
        else:
            setSituationOntheGround(True)
        #获取动画源
        now_resource = self.animationConsole.get_Next_resource()
#         print(self.animationConsole.nowAnimation.nowImageNumber)
        #获取图像，检查翻转
        img = now_resource["图像"]
        mirFlag = isMirrorImage()
        if(mirFlag==True):
            img = img.mirrored(True, False)
        #更新动画
        self.label.setPixmap(QPixmap.fromImage(img))
        
        #Label图像移动
        if(now_resource.get("镜像图像偏移") is not None and mirFlag==True):
            moveX, moveY = now_resource.get("镜像图像偏移")
            self.label.move(100+moveX, 100+moveY)
        elif(now_resource.get("图像偏移") is not None):
            moveX, moveY = now_resource.get("图像偏移")
            if(mirFlag==True):
                self.label.move(100-moveX, 100+moveY)
            else:
                self.label.move(100+moveX, 100+moveY)
        
        #窗口移动
        if(now_resource.get("窗口偏移") is not None):
            moveX, moveY = now_resource.get("窗口偏移")
            #移动窗口
            windowX = self.geometry().x()
            if(moveX!=0 and windowX < self.fairy.windowLocationLimited_X[1]):
                windowX = windowX + moveX
            if(moveY!=0 and windowY < self.fairy.windowLocationLimited_Y[1]):
                windowY = windowY + moveY
            self.move(windowX, windowY)
        #时延
        if(now_resource.get("时延") is not None):
            time.sleep(now_resource.get("时延"))
    
#     def enterEvent(self, event):
#         #鼠标移入事件
# #         self.mouseOnTheLabel = True
#         event.accept()
#         print("")
    def mousePressEvent(self, event):
        # 鼠标点下去事件
        pButton = event.button()
        event.accept()
        if(self.animationConsole.mouseAnimation is None or self.animationConsole.mouseAnimation.get("点击") is None):
            return
      
        for pressAnimation in self.animationConsole.mouseAnimation["点击"]:
            if((pButton==Qt.LeftButton and pressAnimation.get("键位")=="左键")or(pButton==Qt.RightButton and pressAnimation.get("键位")=="右键")):
                if(self.animationConsole.nowAnimation.ID == pressAnimation["当前动画id"]):
                    self.animationConsole.changeAnimationByID(pressAnimation.get("动作id"))
                    #有悬挂点属性的会更改窗口位置，长按不放拖动能移动窗口
                    if(pressAnimation.get("悬挂点") is not None):
                        self.isHangingAnimation=True
                        m_Position = event.windowPos().toPoint() #获取鼠标相对窗口的位置
                        self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标
                        #计算挂点到鼠标位置的差值 
                        hangPoint = pressAnimation.get("悬挂点")
                        move = m_Position - QPoint(100,100) - hangPoint
                        new = QPoint(self.geometry().x(),self.geometry().y())
                        self.move(new + move) #将挂点位置移动到鼠标处
                        self.m_Position = QPoint(100,100) + hangPoint #重置鼠标相对窗口的位置
                                 
        
    def mouseMoveEvent(self, QMouseEvent):
        # 鼠标移动事件
        if(self.isHangingAnimation and Qt.LeftButton):  
            #QMouseEvent.globalPos() 对于整个显示器来说鼠标的坐标
            #self.m_Position 对窗口来说鼠标的坐标
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
        QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        # 鼠标释放事件
        leleaseButton = QMouseEvent.button()
        if(self.animationConsole.mouseAnimation is None or self.animationConsole.mouseAnimation.get("释放") is None):
            return
        for releaseAnimation in self.animationConsole.mouseAnimation["释放"]:
            if((leleaseButton==Qt.LeftButton and releaseAnimation.get("键位")=="左键")or(leleaseButton==Qt.RightButton and releaseAnimation.get("键位")=="右键")):
                if(self.animationConsole.nowAnimation.ID == releaseAnimation.get("当前动画id")):
                    if(releaseAnimation.get("条件")=="不在地上" and isOnTheGround()==False):
                        AnimationID = releaseAnimation.get("动作id")
                        self.animationConsole.changeAnimationByID(AnimationID)
                        if(releaseAnimation.get("取消悬挂")=="是"):
                            self.isHangingAnimation = False
                            self.setCursor(QCursor(Qt.ArrowCursor))
    def wheelEvent(self, event):
        # 鼠标滚轮事件
        if(self.animationConsole.mouseAnimation is None or self.animationConsole.mouseAnimation.get("鼠标滚轮") is None):
            return
        wheelAnimationList = self.animationConsole.mouseAnimation.get("鼠标滚轮")
        for changeAnimation in wheelAnimationList:
            if(changeAnimation.get("滚轮方向")=="向上" and event.angleDelta().y()>0) or (changeAnimation.get("滚轮方向")=="向下" and event.angleDelta().y()<0):#方向向下
                if(changeAnimation.get("条件")=="在地上" and isOnTheGround()==True):
                    if(self.animationConsole.nowAnimation.ID == changeAnimation.get("当前动画id")):
                        self.animationConsole.changeAnimationByID(changeAnimation.get("动作id"))

        
    
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = FairyWindow(fairyID="vat")
    
    win.show()
    sys.exit(app.exec_())
