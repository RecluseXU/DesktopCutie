# -*- coding: utf-8 -*-

'''
Created on 2019年2月21日

@author: RecluseXu
对输入的东西进行匹配
'''
from model.CLASS.JudgeResoult import JudgeResoult
import json

matching_dict = None

def _loading_matching_dict():
    # 读取mapper
    from infoTool.load_Project_Location import get_resourceLocation
    match_mapper_location = get_resourceLocation()+"Manager/TalkWidget/Judgement/CommandMatchingMapper.json"
    global matching_dict
    try:
        with open(match_mapper_location,"r")as f:
            matching_dict = json.load(f)
    except:
        print("读取匹配mapper失败")


def reload_mapper():
    '''
    重新从文件中载入mapper
    '''
    _loading_matching_dict()

def get_matching_dict():
    '''
    获取匹配dict
    '''
    global matching_dict
    if(matching_dict is None):
        reload_mapper()
    return matching_dict

def enable_matching(matching_str):
    '''
    传入匹配项名称,启用匹配项
      执行完毕后会保存状态到文件中
    '''
    global matching_dict
    if(matching_dict is None):
        _loading_matching_dict()
    
    #目标项存在，且被禁用
    if(matching_dict.get(matching_str) is not None and matching_dict.get(matching_str)[1]==0):
        matching_dict[matching_str][1] = 1
    
    save_command_matching_state() # 保存状态到文件

def disable_matching(matching_str):
    '''
    传入匹配项名称,禁用匹配项
    执行完毕后会保存状态到文件中
    '''
    global matching_dict
    if(matching_dict is None):
        _loading_matching_dict()
    
    #目标项存在，且已经启用
    if(matching_dict.get(matching_str) is not None and matching_dict.get(matching_str)[1]==1):
        matching_dict[matching_str][1] = 0
        
    save_command_matching_state() # 保存状态到文件

def save_command_matching_state():
    '''
    保存命令匹配状态到文件中
    文件路径:/resource/Manager/TalkWidget/Judgement/CommandMatchingMapper.json
    '''
    from infoTool.load_Project_Location import get_resourceLocation
    match_mapper_location = get_resourceLocation()+"Manager/TalkWidget/Judgement/CommandMatchingMapper.json"
    global matching_dict
    with open(match_mapper_location, "w")as f:
        json.dump(matching_dict, f, indent=4)
   

def judge(input_str): 
    #匹配命令类型
    #print(inputCommand)
    global matching_dict
    
    if(matching_dict is None):
        _loading_matching_dict()
    for key in list(matching_dict.keys()):
        # 遍历匹配项目、匹配、返回结果
        if(matching_dict[key][1] == 0): # 当命令未被启用 
            continue
        matching_str = matching_dict[key][0]
        if(input_str[:len(matching_str)] == matching_str):
            judge_resoult = JudgeResoult(input_str,True)
            judge_resoult.operation_str = key
            judge_resoult.parameter = input_str[len(matching_str):]
            judge_resoult.judge_type = "CommandMatching"
            return judge_resoult
    return input_str



if __name__=="__main__":
    r = judge("./q")
    print(matching_dict)
    print(r)
    print(r.operation_str)
#     print(command_dict)
#     matching_dict['cmdCommandTransmit'][1]=0
#     save_command_matching_state()