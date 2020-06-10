# -*- coding: utf-8 -*-

'''
Created on 2019年3月21日

@author: RecluseXu
'''

class AnimationMouse(object):
    def __init__(self):
        self.mouse_click_animation_list = None
        self.mouse_release_animation_list = None
        self.mouse_wheel_animation_list = None
    
    def add_mouse_click_animation_change(self, click_key, condition_function_list, now_animation, aim_animation, hang_point):
        '''
        添加点击鼠标事件
        click_key:鼠标上的键
        condition_function_list:条件函数列表
        now_animation:现在播放的动画的动画id
        aim_animation:目标动画的动画id
        hang_point：悬挂点
        '''
        if(self.mouse_click_animation_list is None):
            self.mouse_click_animation_list = []
        click_note = {"键位":click_key, "发生条件":condition_function_list, "当前动画id":now_animation, "目标动画":aim_animation, "悬挂点":hang_point}
        self.mouse_click_animation_list.append(click_note)
    
    def add_mouse_release_animation_change(self, click_key, condition_function_list, now_animation, aim_animation, hang_point, cancel_hang):
        '''
        添加释放鼠标事件
        click_key:鼠标上的键    type:QtCore.Qt中的值
        condition_function_list:条件函数列表
        now_animation:现在播放的动画的动画id
        aim_animation:目标动画的动画id
        hang_point：悬挂点
        cancel_hang：取消悬挂
        '''
        if(self.mouse_release_animation_list is None):
            self.mouse_release_animation_list = []
        release_note = {"键位":click_key, "发生条件":condition_function_list, "当前动画id":now_animation, "目标动画":aim_animation, "悬挂点":hang_point, "取消悬挂":cancel_hang}
        self.mouse_release_animation_list.append(release_note)
    
    def add_mouse_wheel_animation_change(self, mouse_wheel_operation, condition_function_list, now_animation, aim_animation):
        '''
        添加鼠标滚路事件
        '''
        if(self.mouse_wheel_animation_list is None):
            self.mouse_wheel_animation_list = []
        wheel_note = {"滚轮操作":mouse_wheel_operation, "发生条件":condition_function_list, "当前动画id":now_animation, "目标动画":aim_animation}
        self.mouse_wheel_animation_list.append(wheel_note)
    
    