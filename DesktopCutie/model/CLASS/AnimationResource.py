# -*- coding: utf-8 -*-
'''
Created on 2019年3月21日

@author: RecluseXu
'''

class AnimationResource(object):
    def __init__(self, resource_id, resource_base_location):
        self.resource_id = resource_id
        self.base_location = resource_base_location
        self.picture_list = None
        self.total_frame_length = None
    
    def add_resouce(self, picture, window_excursion, picture_excursion, mirror_picture_excursion, sleep_time_extended, frame_amount_extended,picture_location):
        '''
        添加<图像资源>
        picture:帧图像     type:QImage
        window_excursion：窗口偏移    type:[int,int]
        picture_excursion：图像偏移    type:[int,int]
        mirror_picture_excursion: 镜像图像偏移     type:[int,int]
        sleep_time_extended：时延    type:float
        frame_amount_extended：帧延    type:int
        '''
        if(self.picture_list is None):
            self.picture_list = []
            self.total_frame_length = 0
        
        # 处理None造成的差异
        if(window_excursion is None):  # 没有窗口偏移
            window_excursion = [0,0]
        if(picture_excursion is None): # 没有图像偏移
            picture_excursion = [0,0]
        if(mirror_picture_excursion is None): # 没有镜像图像偏移
            mirror_picture_excursion = [0,0]
        if(sleep_time_extended is None): # 没有时延
            sleep_time_extended = 0
        if(frame_amount_extended is None): # 没有帧延
            frame_amount_extended = 0
        
        # 添加记录
        register_note = {"图像":picture, "窗口偏移":window_excursion, "图像偏移":picture_excursion, "镜像图像偏移":mirror_picture_excursion, "时延":sleep_time_extended, "帧延":frame_amount_extended, "资源路径":picture_location}
        self.picture_list.append(register_note)
        # 更新总帧长
        self.total_frame_length = len(self.picture_list)
    