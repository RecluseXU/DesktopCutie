# -*- coding: utf-8 -*-
'''
Created on 2019年1月8日

@author: RecluseXu
'''
import xml.etree.cElementTree as ET
from model.Animation import Animation
from model.AnimationConsole import AnimationConsole
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt
from PyQt5.Qt import QPoint
from infoTool.situation import chineseSituationConditionTransformToJudgeFunction

def imageScale(img,scaleProportion):
    # 按比例缩放图片
    newWidth = int(img.size().width()* scaleProportion)
    newHeight = int(img.size().height()* scaleProportion)
    # 变更图片大小，按比例缩放，平滑缩放
    return img.scaled(newWidth, newHeight, Qt.KeepAspectRatio, Qt.SmoothTransformation)

def load_animation_from_xml(fairyID):
    print("读取动作xml......",end="")
    
    from infoTool.load_Fairy_From_XML_File import get_FairyInfo 
    from infoTool.load_Project_Location import get_TheCuiteFolderLocation
    
    xml_add = get_FairyInfo(fairyID).resourceLocation
    animationSizeScale = get_FairyInfo(fairyID).animationSizeScale # 获取图片缩放比例
#     print(xml_add)
    animation_Dict = {}
    
    #载入xml文件进行分析
    tree = ET.parse(xml_add) 
    root = tree.getroot()   # 获取根节点
    # 载入动画图片信息
    for child in root.find("动作注册"):   
        aAnimation = Animation(child.attrib.get("id"), child.attrib.get("逻辑id").split(","), child.attrib.get("资源id"))
        aAnimation.defaultLogicID = aAnimation.logic[0]
        aAnimation.nowLogicID = aAnimation.defaultLogicID
        logicDict = {}
        logicReplaceDict = {}
        for log_child in root.find("动作逻辑"):
            for i in range(0,len(aAnimation.logic)):
                if(aAnimation.logic[i] == log_child.attrib.get("id")):
                    logicLIST = []
                    # 发生频率转为发生阀值，以方便用random处理事件
                    before_probability = 0
                    for log2_child in log_child:
                        aLogic = log2_child.attrib.copy()
                        if(log2_child.tag == "下一个动作"):
                            now_Probability_str = aLogic.get("发生频率")
                            if(now_Probability_str is not None):
                                now_Probability = int(now_Probability_str)
                            else:
                                now_Probability = 1
                            aLogic["发生阀值"] = before_probability + now_Probability
                            before_probability = before_probability + now_Probability
                            if(now_Probability_str is not None):
                                aLogic.pop("发生频率")
                            logicLIST.append(aLogic)
                        if(log2_child.tag == "逻辑更替"):
                            logicReplaceDict[aLogic.get("发生条件")] = aLogic
                            if(aLogic.get("强制更替")=="是"):
                                aAnimation.haveCompelChangeLogicItem = True
                        if(log2_child.tag == "动作更替"):
                            chinese_condition = log2_child.attrib["发生条件"]
                            judgeFunction = chineseSituationConditionTransformToJudgeFunction(chinese_condition)
                            log2_child.attrib["发生条件"] = judgeFunction
                            if(log2_child.attrib.get("强制更替")=="是"):
                                aAnimation.haveCompelChangeAnimationItem = True
                            
                            if(aAnimation.conditionChangeAnimation is None):
                                aAnimation.conditionChangeAnimation=[]
                            aAnimation.conditionChangeAnimation.append(log2_child.attrib)
    
                        if(log2_child.tag == "状态修改"):
                            situationChangeList = []
                            # 获取状态修改的属性名 与 值
                            key = list(aLogic.keys())[0]
                            value = aLogic.get(key)
                            # 根据属性名与值转化为对应的设置函数，然后保存，留待动画播放完毕后执行。
                            from infoTool.situation import chineseSituationConditionTransformToSetSituationFunction
                            setSituationFunction = chineseSituationConditionTransformToSetSituationFunction(key, value)
                            situationChangeList.append(setSituationFunction)

                            aAnimation.situationChange = situationChangeList
                            
                    logicDict[aAnimation.logic[i]] = logicLIST
                    aAnimation.sumProbabilityValue = before_probability
        aAnimation.logic = logicDict
        if(len(logicReplaceDict.keys())!=0):
            aAnimation.conditionReplaceLogic = logicReplaceDict
        
        
        animationResourceElement = root.find("动作资源")
        for source_set in animationResourceElement:    
            #将资源绝对路径与动画集路径结合，得到动画资源集的绝对路径
            sources_set_location = get_TheCuiteFolderLocation(fairyID) + source_set.attrib.get("资源地址")
            
            if(aAnimation.resource == source_set.attrib.get("id")):
                resourceSet = []
                for a_source in source_set: 
                    # 将动画资源集绝对路径与图像名称结合，得到图像绝对路径
                    imgAddress = sources_set_location + a_source.attrib["图像"] 
                    # 由于不能保存QPixmap对象，这里将图片地址转换为QImage对象保存                  
                    img = QImage(imgAddress)
                    img = imageScale(img,animationSizeScale)# 缩放图片
                    a_source.attrib["图像"] = img
                    if(a_source.attrib.get("窗口偏移")is not None):
                        a_source.attrib["窗口偏移"] = [int(x) for x in a_source.attrib["窗口偏移"].split(",")]
                    if(a_source.attrib.get("图像偏移")is not None):
                        a_source.attrib["图像偏移"] = [int(int(x)*animationSizeScale) for x in a_source.attrib["图像偏移"].split(",")]                      
                    if(a_source.attrib.get("镜像图像偏移")is not None):
                        a_source.attrib["镜像图像偏移"] = [int(int(x)*animationSizeScale) for x in a_source.attrib["镜像图像偏移"].split(",")]  
                    if(a_source.attrib.get("时延") is not None):
                        a_source.attrib["时延"] = float(a_source.attrib["时延"])
                    if(a_source.attrib.get("帧延") is not None):
                        a_source.attrib["帧延"] = int(a_source.attrib["帧延"])
                    resourceSet.append(a_source.attrib)
                aAnimation.animationLength = len(source_set)          
                aAnimation.resource = resourceSet
                
            aAnimation.resetAnimation()
        animation_Dict[aAnimation.ID] = aAnimation
    init_AnimationID = root.find("初始动画").attrib.get("动作id")
    init_Animation = animation_Dict[init_AnimationID]
    animationConsole = AnimationConsole(animation_Dict, init_Animation)
    
    mouseAnimationELE = root.find("鼠标动画")
    if(mouseAnimationELE is not None):
        mouseAnimationDict={}
        for ami in mouseAnimationELE:
            if(ami.tag == "点击"):
                checkAnimationList = []
                for c in ami:
                    a = c.attrib
                    animation_Dict[a.get("当前动画id")] #尝试获取动画
                    animation_Dict[a.get("动作id")]
                    if(a.get("悬挂点")is not None):
                        x,y=[int(x) for x in a["悬挂点"].split(",")]
                        a["悬挂点"] = QPoint(x,y)
                    checkAnimationList.append(a)
                mouseAnimationDict["点击"] = checkAnimationList
            if(ami.tag == "释放"):
                releaseAnimationList = []
                for c in ami:
                    a = c.attrib
                    animation_Dict[a.get("当前动画id")] #尝试获取动画
                    animation_Dict[a.get("动作id")]             
                    releaseAnimationList.append(a)
                mouseAnimationDict["释放"] = releaseAnimationList
            if(ami.tag == "鼠标滚轮"):
                wheelAnimationList = []
                for c in ami:
                    a = c.attrib
                    animation_Dict[a.get("当前动画id")]#尝试获取动画
                    animation_Dict[a.get("动作id")]
                    wheelAnimationList.append(a)
                mouseAnimationDict["鼠标滚轮"] = wheelAnimationList
        animationConsole.mouseAnimation = mouseAnimationDict
    return animationConsole

def getLoadAnimationQThread(fairyID):
    from model.MyThread import MyThread
    return MyThread(load_animation_from_xml, fairyID)
    
if __name__ == '__main__':
#     print(animationXMLLocation)
    l = load_animation_from_xml("demo")
    print(l.animationDict["站立"].logic)
    
#     for i in range(14):
#         k = l.animationDict.get("闲置坐转闲置站立").get_next_resource()
#         print(k)
#     l.animationDict["浮空"].printINFO()
#     print(l.mouseAnimation)