# -*- coding: utf-8 -*-
'''
Created on 2019年1月9日

@author: RecluseXu
'''

import random
from infoTool.situation import isOnTheGround

class Animation(object):
    def __init__(self, animationID, logic, resource):
        self.ID = animationID # 动画ID，唯一标识一个动画。type=str
        self.logic = logic # 动画逻辑，记录着播放玩动画后接下应该播放什么动画，及播放频率。
                            # key="逻辑id",value=[{"动作id":str, "发生阀值":int}]
        self.resource = resource # 动画资源，保存着动画图片与窗口偏移。
        self.defaultLogicID = self.logic[0] #动画默认逻辑id
        
        
        self.situationChange = None #状态更替
        self.animationLength = None # 动画帧数长度
        self.conditionReplaceLogic = None # 逻辑更替，当达到某个条件的时候，用新的逻辑取代留的逻辑时使用。
                                            #key="更替条件",value={"发生条件":str, "逻辑id"=str, "强制更替"="是"}
        self.haveCompelChangeLogicItem = False #是否存在强制逻辑更替
        self.conditionChangeAnimation = None # 动画更替，当达到某个条件的时候，用新的动画取代现在的动画。
                                            # [{"发生条件":fuction, "动作id"=str, 强制更替=boolean} ]
        self.haveCompelChangeAnimationItem = False #是否存在强制动画更替
   
        self.sumProbabilityValue = 0 # 动画逻辑中，全部下一动画频率之和
        self.nowLogicID = None # 当前逻辑id
        self.nowImageNumber = 0 # 当前动画帧的数号
        self.nowProlongTime = 0 # 当前延长帧
        
    def check_logicReplace(self, isEnd=True):
#         检查逻辑更替
#         isEnd，boolean,是否是动画末尾。
        if(isEnd==False and self.haveCompelChangeLogicItem==False): #当没有强制替代，却在动画过程中被调用
            return
        
        # 逻辑更替
        if(self.conditionReplaceLogic is not None):
            conditionKeyList = self.conditionReplaceLogic.keys()  
            for conditionKey in conditionKeyList:
                if(conditionKey == "在地上"):
                    if(isOnTheGround()==True):
                        self.nowLogicID = self.conditionReplaceLogic[conditionKey]["逻辑id"]
    def check_compelChangeAnimation(self, isEnd=True):
        # 检查动画更替
        if(isEnd==False and self.haveCompelChangeAnimationItem == False): #当没有强制替代，却在动画过程中被调用
            return
        if(self.conditionChangeAnimation is not None):
            for conditionChangeDict in self.conditionChangeAnimation:
                if(conditionChangeDict["发生条件"]()):
                    return conditionChangeDict["动作id"]
    def get_next_resource(self):
    # 获取下一个动画源
        #在动画播放过程中，检查逻辑更替
        self.check_logicReplace(isEnd=False)
        #在动画播放过程中，检查动画更替
        a = self.check_compelChangeAnimation(isEnd=False)
        if(a is not None):
            return a
        
        if(self.nowProlongTime==0):#当当前帧延为0，无需拖延时
            #更新新的帧延
            if(self.get_now_resource().get("帧延") is not None):
                self.nowProlongTime = self.get_now_resource().get("帧延")
            
            # 当动画没超出长度时播放,即动画未播放完毕时。
            #    更新帧数，返回对应源
            if(self.nowImageNumber < self.animationLength): 
                self.nowImageNumber = self.nowImageNumber+1
                return self.get_now_resource()
            # 当当前帧号码超出，既动画播放完毕
            else:       
                #执行"状态修改"内容
                if(self.situationChange is not None):
                    for function in self.situationChange: 
                        function()
                # 检查逻辑更替
                self.check_logicReplace()
                # 检查动画更替
                a = self.check_compelChangeAnimation()
                if(a is not None):
                    return a
                
                #重置现在播放数
                self.resetNowImageNumber()
                #随机数抽签下一动画
                randomNum = random.randint(0,self.sumProbabilityValue) 
                for nextAnimation in self.logic[self.nowLogicID]:
                    if(randomNum <= nextAnimation.get("发生阀值")):
                        return nextAnimation.get("动作id")
        #当前帧延不为0,返回当前源
        else:
            self.nowProlongTime = self.nowProlongTime-1
            return self.get_now_resource()
    
    
    def get_now_resource(self):
        return self.resource[self.nowImageNumber-1]
        
    def resetAnimation(self):# 重置当前动画帧与逻辑
        self.nowLogicID = self.defaultLogicID
        self.nowImageNumber = 0
    def resetNowLogic(self):
        self.nowLogicID = self.defaultLogicID
    def resetNowImageNumber(self):
        self.nowImageNumber = 0
        
        
    def printINFO(self):
#         print("id",self.ID)
#         print("逻辑",self.logic)
        print("逻辑更替",self.conditionReplaceLogic)
#         print("动画资源",self.resource)
        print("默认逻辑的逻辑id",self.defaultLogicID)
#         print("最大概率阀值",self.sumProbabilityValue)
        print("现在的逻辑id号",self.nowLogicID)
#         print("现在帧数",self.nowImageNumber)
#         print("总帧数",self.animationLength)