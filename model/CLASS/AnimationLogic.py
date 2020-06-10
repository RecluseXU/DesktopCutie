# -*- coding: utf-8 -*-
'''
Created on 2019年3月20日

@author: RecluseXu
'''

class AnimationLogic(object):
    def __init__(self, logicID):
        self.logicID = logicID
        self.next_animation_list = [] # 用于保存<下一个动画>
        self.sum_probability_threshold = 0 # 其下所有<下一个动画>的发生阀值的和
        
        self.logic_replace_list = None # 逻辑更替
        self.have_compel_logic_replace = None # 有强制逻辑更替标志位
        
        self.animation_replace_list = None # 动作更替
        self.have_compel_animation_replace = None # 有强制动作更替标志位
        
        self.situation_change_list = None # 状态更变
        
    def add_next_animation(self, next_animation_id, probability_str="1"):
        '''
        添加<下一个动画>
        next_animation_id:下一个动画的id
        probability_str:发生频率(str)
        '''
        if(probability_str is None):
            probability_str = 1
        now_probability = int(probability_str)
        threshold = self.sum_probability_threshold + now_probability
        self.sum_probability_threshold = self.sum_probability_threshold + now_probability
        
        next_note = {"动画id":next_animation_id, "发生阀值":threshold}
        self.next_animation_list.append(next_note)
    
    def add_logic_replace(self, replace_logic_id, condiction_function_list, compel_change=False):
        '''
        添加<逻辑更替>
        replace_logic_id:替换逻辑id    type:str
        condiction_function_list:条件函数列表    type:[function(只返回bool)]
        compel_change:强制更替标志位    type:bool
        '''
        
        if(self.logic_replace_list is None):
            self.logic_replace_list = []
            self.have_compel_logic_replace = False
        
        # 如果添加的记录中有强制更替，那么改变标志位
        if(self.have_compel_logic_replace==False and compel_change==True):
            self.have_compel_logic_replace = True    
        
        change_note = {"发生条件":condiction_function_list, "逻辑id":replace_logic_id, "强制更替":compel_change}
        self.logic_replace_list.append(change_note)
        
    
    def add_animation_replace(self, replace_animation_id, condiction_function_list, compel_change=False):
        '''
        添加<动作更替>
        replace_animation_id:目标动画id    type:str
        condiction_function_list:判断函数列表    type:[function(只返回bool)]
        compel_change:强制更替标志位    type:bool
        
        '''
        if(self.animation_replace_list is None):
            self.animation_replace_list = []
            self.have_compel_animation_replace = False
        
        # 如果添加的记录中有强制更替，那么改变标志位
        if(self.have_compel_animation_replace==False and compel_change==True):
            self.have_compel_animation_replace = True
        
        change_note = {"发生条件":condiction_function_list, "动作id":replace_animation_id, "强制更替":compel_change}
        self.animation_replace_list.append(change_note)
        
    def add_situation_change(self, set_function, change_moment, condition_function_list):
        '''
        添加<状态修改>
        set_function:修改状态的函数    type:func
        change_moment:修改时机  type:str 有两种可能出传入:"start"与"end"
        condition_function_list:判断函数列表    type:[function(只返回bool)]
        '''
        if(self.situation_change_list is None):
            self.situation_change_list = []
            
        if(condition_function_list is None):
            condition_function_list = []
        if(change_moment is None):
            change_moment = "end"    
        
        situation_note = {"发生条件":condition_function_list, "状态修改函数":set_function, "修改时机":change_moment}
        self.situation_change_list.append(situation_note)
        
        
        
        
        