# -*- coding: utf-8 -*-
'''
Created on 2019年3月26日

@author: RecluseXu
'''
from infoTool.load_Project_Location import get_FairyInfoNote_folder_location
import json


animation_general_info_dict = None

def _load_all_animation_general_info(fairy_id):
    '''
    从文件中读取精灵动画概要信息
    概要信息文件在创建FairyFrame实例时会被生成
    '''
    global animation_general_info_dict
    general_info_folder_loacation = get_FairyInfoNote_folder_location()+fairy_id+".json"
    try:
        with open(general_info_folder_loacation, "r")as f:
            general_info = json.load(f)
        animation_general_info_dict["fairy_id"] = general_info
    except:
        return 
    
    return general_info

def save_general_fairy_info_to_file(fairy_id, animation_dict, logic_dict, resource_dict, mouse_animation, signal_animation, init_AnimationID):
    '''
    将精灵动画的大体信息保存在一个文件中，以便以后浏览。
    '''
    print("保存精灵动画的大体信息")
    general_info_dict = {"注册信息":list(animation_dict.keys()), 
                         "逻辑信息":list(logic_dict.keys()), 
                         "资源信息":list(resource_dict.keys()), 
                         "初始动画":init_AnimationID}
    general_info_location = get_FairyInfoNote_folder_location()+fairy_id+".json"
    print(general_info_location)
    with open(general_info_location, "w") as f:
        json.dump(general_info_dict, f)


def get_animation_general_info(fairy_id):
    '''
    获取精灵动画概要信息
    '''
    global animation_general_info_dict
    
    if(animation_general_info_dict is None):
        animation_general_info_dict = {}
    
    # 检查当前已经存入内存的记录
    animation_general_info = animation_general_info_dict.get(fairy_id)
    # 未存入内存
    if(animation_general_info is None):
        # 尝试去获取
        animation_general_info = _load_all_animation_general_info(fairy_id)
    
    return animation_general_info
            
    