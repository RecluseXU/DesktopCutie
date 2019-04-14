# -*- coding: utf-8 -*-
'''
Created on 2019年1月9日

@author: RecluseXu
'''

class AnimationConsole(object):
    #动画控制
    def __init__(self,animationDict,init_Animation):
        self.animationDict = animationDict # 动画集
        self.nowAnimation = init_Animation # 当前动画实例，Animation类型。
        self.mouseAnimation = None
    
    def get_Next_resource(self):
        now_resource = self.nowAnimation.get_next_resource() #获取下一个源的信息
        if(type(now_resource) == type("AnimationID")): #如果返回来的不是图片，是一个id
            self.nowAnimation = self.animationDict[now_resource]
            return self.nowAnimation.get_next_resource()
        else:
            return now_resource

    def changeAnimationByID(self,AnimationID):
        self.nowAnimation.resetNowImageNumber()
        self.nowAnimation = self.animationDict.get(AnimationID)
        self.nowAnimation.resetNowLogic()