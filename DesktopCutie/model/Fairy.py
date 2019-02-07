# -*- coding: utf-8 -*-
'''
Created on 2019年1月11日

@author: RecluseXu
'''

class Fairy(object):
    def __init__(self,the_id):
        self.id = the_id #Fairy的ID
        self.name = None #Fairy的名字
        self.fairySetXMLLocation = None #Fairy设置文档的路径
        self.resourceLocation = None #资源路径
        self.initWindowLocation = None #窗口初始位置
        self.windowLocationLimited_X = None #对窗口坐标的限制
        self.windowLocationLimited_Y = None
        self.animationSizeScale = None #图片缩放比例
        
        self.author = None #作者信息
        self.version = None #版本信息
        self.license = None #许可信息
        self.fairyINFO = None #精灵信息