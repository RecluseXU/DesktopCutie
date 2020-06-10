# -*- coding: utf-8 -*-
'''
Created on 2019年3月21日

@author: RecluseXu
'''

class AnimationRegister(object):
    def __init__(self, animation_id, logic_id, resource_id):
        self.animation_id = animation_id
        self.logic_id = logic_id
        self.resource_id = resource_id
    
    def __str__(self):
        return "动画id:"+self.animation_id+"\t逻辑id:"+self.logic_id+"\t资源id:"+self.resource_id