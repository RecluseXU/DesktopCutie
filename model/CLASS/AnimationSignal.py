# -*- coding: utf-8 -*-
'''
Created on 2019年3月21日

@author: RecluseXu
'''
class AnimationSignal(object):
    def __init__(self):
        self.signal_animation_dict = None
    
    def add_signal_animation(self, signal_name, condition_function_list, now_animation, aim_animation):
        '''
        添加<信号动画>
        '''
        if(self.signal_animation_dict is None):
            self.signal_animation_dict = {}
        signal_note = {"信号名称":signal_name, "发生条件":condition_function_list, "当前动画id":now_animation, "目标动画":aim_animation}
        
        self.signal_animation_dict[signal_name] = signal_note
        
    def __str__(self):
        if(self.signal_animation_dict is None):
            return "未设置信号动画"
        else:
            return_str = ""
            for signal_note in self.signal_animation_dict.values():
                return_str = return_str + signal_note["信号名称"]+":"+signal_note["目标动画"]+"\t"
            return return_str