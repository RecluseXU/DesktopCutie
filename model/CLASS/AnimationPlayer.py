# -*- coding: utf-8 -*-
'''
Created on 2019年3月21日

@author: RecluseXu
'''

from model.CLASS.Situation import check_all_condiction_in_list
import random


class AnimationPlayer(object):
    def __init__(self, animation_register, animation_logic, animation_resource, func_get_register_by_id, func_get_logic_by_id, func_get_resource_by_id):
        '''
        初始化函数
        animation_register:当前动画的注册信息    type:AnimationRegister
        animation_logic:当前动画的逻辑    type:AnimationLogic
        animation_resource:当前动画的资源    type:AnimationResource
        get_logic_by_id_func:通过逻辑id获取逻辑(AnimationLogic对象)的函数
        '''
        
        self.now_register = animation_register # 当前动画的注册信息
        self.now_logic = animation_logic # 当前动画的逻辑
        self.now_resource = animation_resource # 当前动画的资源
        
        self.now_frame_number = 0 # 当前动画帧的数号
        self.now_frame_extend = 0 # 当前帧延 
        self.have_use_frame_extend = False # 是否已经应用帧延
        
        # 辅助函数部分，用于从AnimationConsole实例中获取信息
        self.function_get_register_by_id = func_get_register_by_id # 获取动画注册信息的函数
        self.function_get_logic_by_id = func_get_logic_by_id # 获取动画逻辑的函数
        self.function_get_resource_by_id = func_get_resource_by_id # 获取动画资源的函数
        
    def get_now_frame(self):
        '''
        根据当动画帧的数号、返回当前帧记录
        '''
#         print(self.now_resource.picture_list[self.now_frame_number])
        return self.now_resource.picture_list[self.now_frame_number]
    
    def change_animation_by_animation_id(self, animation_id):
        '''
        更改现在播放的动画。
        这个函数会根据传入的动画id来更变动画，过程中会刷新 动画注册、逻辑、资源、当前帧数信息
        '''
        self.now_register = self.function_get_register_by_id(animation_id)       
        self.now_logic = self.function_get_logic_by_id(self.now_register.logic_id)
        self.now_resource = self.function_get_resource_by_id(self.now_register.resource_id)
        self.now_frame_number = 0
        #刷新帧延
        self.now_frame_extend = 0
        self.have_use_frame_extend = False
    
    def check_logic_replace(self, is_start_moment=False):
        '''
        检查<逻辑更替>
        moment:执行的时机
        '''
        
        # 没有逻辑更替
        if(self.now_logic.logic_replace_list is None):
            return
        # 在开头的时候检查，所有逻辑替代没有强制更替项目，直接返回
        if(is_start_moment==True and self.now_logic.have_compel_logic_replace==False):
            return
        
        # 将逻辑更替记录遍历
        for logic_replace_note in self.now_logic.logic_replace_list:
            # 如果现在是开头检查，非强制更替项目就跳过
            if(is_start_moment==True and logic_replace_note["强制更替"]==False):
                continue
            # 判断所有条件
            condition_check_resoult = check_all_condiction_in_list(logic_replace_note["发生条件"])
            
            # 所有条件都满足，执行更替
            if(condition_check_resoult == True):
                aim_logic_id = logic_replace_note["逻辑id"]
                self.now_logic = self.function_get_logic_by_id(aim_logic_id)
    
    def check_situation_change(self,is_start_moment=False):   
        '''
        检查<状态修改>
        '''
        # 没有状态修改
        if(self.now_logic.situation_change_list is None):
            return
        # 在不是第一帧时，进行开头检查时
        if(self.now_frame_number!=0 and is_start_moment==True):
            return
        
        
        for situation_change_note in self.now_logic.situation_change_list:
            # 开头检查时，修改时机不为"start"的，会直接跳过。
            if(is_start_moment==True and situation_change_note["修改时机"]!="start"):
                continue
            # 在结尾检查时，修改时机不为"end"的，会直接跳过
            if(is_start_moment==False and situation_change_note["修改时机"]!="end"):
                continue
            
            # 进行发生条件判断
            check_resoult = check_all_condiction_in_list(situation_change_note["发生条件"])
            if(check_resoult==True):
#                 print("状态修改",end="")
                situation_change_note["状态修改函数"]() # 执行状态修改函数
#                 print("完毕")
    
    def exchange_to_next_animation(self):
        '''
        进行<下一个动作>
        '''
        #随机数抽签下一动画
        randomNum = random.randint(0,self.now_logic.sum_probability_threshold) 
        for next_note in self.now_logic.next_animation_list:
            if(randomNum <= next_note.get("发生阀值")):
                # 将下一个动画变为当前动画
                self.change_animation_by_animation_id(next_note["动画id"])
                break
                
                
    def check_animation_change(self, is_start_moment=False):
        '''
        检查<动作更替>
        '''
        # 没有动作更替
        if(self.now_logic.animation_replace_list is None):
            return
        
        # 是开头检查,却没有强制变更，直接跳过
        if(is_start_moment==True and self.now_logic.have_compel_animation_replace==False):
            return 
        
        for replace_note in self.now_logic.animation_replace_list:
            condition_resoult = check_all_condiction_in_list(replace_note["发生条件"])
            if(condition_resoult == True):
                self.change_animation_by_animation_id(replace_note["动作id"])
        
    def get_next_frame(self):
        '''
        获取下一帧图像
        
        一些记录与想法：
        由于逻辑更替会更改逻辑，而状态修改时根据逻辑来的，所以逻辑更替应该在状态修改前，无论是在开头检查还是结尾检查
        '''
        #检查<动画更替>
        self.check_animation_change(is_start_moment=True)
        #检查<逻辑更替>
        self.check_logic_replace(is_start_moment=True)
        #检查<状态修改>
        self.check_situation_change(is_start_moment=True)
#         print("逻辑通过!")
        
        # 帧延相关
        if(self.have_use_frame_extend == False): # 应用帧延，每一帧都应该只应用一次
            self.now_frame_extend = self.now_resource.picture_list[self.now_frame_number]["帧延"]
            self.have_use_frame_extend = True
        
        if(self.now_frame_extend > 0): # 当前帧延判断，当大于0时,返回当前帧即可达到延长显示的效果
            self.now_frame_extend = self.now_frame_extend - 1
            return self.get_now_frame()
        
#         print("帧延通过")
        
        # 当动画没超出长度时播放,即动画未播放完毕时
        if(self.now_frame_number < self.now_resource.total_frame_length-1):
            # 获取当前帧
            the_return_frame = self.get_now_frame()
            
            self.now_frame_number = self.now_frame_number + 1
            self.have_use_frame_extend = False # 帧延重置
            
        
        
        # 当当前帧号码超出，既动画播放完毕
        else: 
            
            the_return_frame = self.get_now_frame()
            self.have_use_frame_extend = False # 帧延重置
            
            # 检查<逻辑更替>
            self.check_logic_replace(is_start_moment=False)
            # 检查<状态修改>
            self.check_situation_change(is_start_moment=False)
            # 检查动画更替
            self.check_animation_change(is_start_moment=False)
            
            #随机数抽签下一动画
            self.exchange_to_next_animation()
            
#         print(the_return_frame)
        return the_return_frame


        