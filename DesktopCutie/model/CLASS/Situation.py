# -*- coding: utf-8 -*-
'''
Created on 2019年3月20日

@author: RecluseXu
'''
def check_all_condiction_in_list(condition_function_list):
    '''
    根据传入的条件函数列表，依次执行函数，综合结果，给出条件成功与否
    '''
    the_judge_flag = True
    for func in condition_function_list:
        if(func() == False):
            return False
    
    return the_judge_flag

class Situation(object):
    '''
    状态类，用于保存动画状态
    '''
    situation_onTheGround = False # 在地上标志位
    situation_mirrorImage = False # 镜像图像标志位
    
    def isOnTheGround(self): # 在地上吗？---获取是否在地上状态
        return self.situation_onTheGround
    
    def isNotOnTheGround(self): # 不在地上吗？
        return not self.situation_onTheGround
    
    
    def setSituationOntheGround(self, situate): # 设置是否在地上状态
        if(self.situation_onTheGround != situate):
            self.situation_onTheGround = situate
            
    def setSituationOntheGround_Yes(self): # 设置,是在地上状态
        self.situation_onTheGround = True
        
    def setSituationOntheGround_No(self): # 设置,不是是在地上状态
        self.situation_onTheGround = False
        
    def setSituationOntheGround_Contrary(self): # 设置，相反的 是否在地上状态
        self.situation_onTheGround = not self.situation_onTheGround
        
    def isMirrorImage(self): 
        # 获取图像翻转是否启用
        return self.situation_mirrorImage
    
    def is_not_MirrorImage(self):
        # 获取图像翻转是否不启用
        return not self.situation_mirrorImage
    
    def setMirrorImage(self, situate): # 设置图像翻转是否开启
        if(self.situation_mirrorImage != situate):
            self.situation_mirrorImage = situate
            
    def setSituationMirrorImage_Yes(self): # 开启图像翻转
        self.situation_mirrorImage = True
        
    def setSituationMirrorImage_No(self): # 关闭图像翻转
        self.situation_mirrorImage = False
        
    def setContraryMirrorImage(self): # 将图像翻转状态设置为与当前状态相反
        self.situation_mirrorImage = not self.situation_mirrorImage
    
    
    def transform_condition_str_list_to_judge_function_list(self, condition_list):
        # 输入给定状态条件中文名称，返回判断函数
        condition_function_list = []
        for condition_str in condition_list:
            if(condition_str == "着陆"):
                condition_function_list.append(self.isOnTheGround)
            elif(condition_str == "不着陆"):
                condition_function_list.append(self.isNotOnTheGround)
            elif(condition_str == "镜像图像"):
                condition_function_list.append(self.isMirrorImage)
            elif(condition_str == "不镜像图像"):
                condition_function_list.append(self.is_not_MirrorImage)
                
                
        return condition_function_list
    
    def transform_set_str_to_set_function(self, situation_str, value_str):
        '''
        将期望的设置转化为设置函数
        '''
        if(situation_str == "水平翻转"):
            if(value_str == "是"):
                return self.setSituationMirrorImage_Yes
            if(value_str == "否"):
                return self.setSituationMirrorImage_No
            if(value_str == "相反"):
                return self.setContraryMirrorImage
        if(situation_str == "着陆"):
            if(value_str == "是"):
                return self.setSituationOntheGround_Yes
            if(value_str == "否"):
                return self.setSituationOntheGround_No
            if(value_str == "相反"):
                return self.etSituationOntheGround_Contrary()