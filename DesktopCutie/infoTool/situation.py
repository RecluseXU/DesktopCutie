# -*- coding: utf-8 -*-
'''
Created on 2019年1月13日

@author: RecluseXu
'''


situation_onTheGround = False
situation_mirrorImage = False

def isOnTheGround():
    #在地上吗？---获取是否在地上状态
    global situation_onTheGround
    return situation_onTheGround
def isNotOnTheGround():
    #不在地上吗？
    global situation_onTheGround
    return not situation_onTheGround
def setSituationOntheGround(situate):
    #设置是否在地上状态
    global situation_onTheGround
    if(situation_onTheGround != situate):
        situation_onTheGround = situate
def setSituationOntheGround_Yes():
    #设置,是在地上状态
    global situation_onTheGround
    situation_onTheGround = True
def setSituationOntheGround_No():   
    #设置,不是是在地上状态
    global situation_onTheGround
    situation_onTheGround = False
def setSituationOntheGround_Contrary():
    global situation_onTheGround
    situation_onTheGround = not situation_onTheGround
def isMirrorImage():
    #获取图像翻转是否启用
    global situation_mirrorImage
    return situation_mirrorImage
def setMirrorImage(situate):
    #设置图像翻转是否开启
    global situation_mirrorImage
    if(situation_mirrorImage != situate):
        situation_mirrorImage = situate
def setSituationMirrorImage_Yes():
    #开启图像翻转
    global situation_mirrorImage
    situation_mirrorImage = True
def setSituationMirrorImage_No():
    #关闭图像翻转
    global situation_mirrorImage
    situation_mirrorImage = False
def setContraryMirrorImage():
    #将图像翻转状态设置为与当前状态相反
    global situation_mirrorImage
    situation_mirrorImage = not situation_mirrorImage

def chineseSituationConditionTransformToJudgeFunction(situationChinese):
    # 输入给定状态条件中文名称，返回判断函数
    if(situationChinese == "在地上"):
        return isOnTheGround
    elif(situationChinese == "不在地上"):
        return 
def chineseSituationConditionTransformToSetSituationFunction(situationChineseKey, situationChineseValue):
    if(situationChineseKey == "水平翻转"):
        if(situationChineseValue == "是"):
            return setSituationMirrorImage_Yes
        if(situationChineseValue == "否"):
            return setSituationMirrorImage_No
        if(situationChineseValue == "相反"):
            return setContraryMirrorImage
    if(situationChineseKey == "在地上"):
        if(situationChineseValue == "是"):
            return setSituationOntheGround_Yes
        if(situationChineseValue == "否"):
            return setSituationOntheGround_No
        if(situationChineseValue == "相反"):
            return setSituationOntheGround_Contrary()

if __name__ == '__main__':
    setSituationOntheGround(True)
    print(isOnTheGround())
    setSituationOntheGround(False)
    print(isOnTheGround())