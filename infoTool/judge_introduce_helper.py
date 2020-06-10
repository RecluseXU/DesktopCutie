# -*- coding: utf-8 -*-
'''
Created on 2019年3月1日

@author: RecluseXu
'''

judge_introduce_dict = None

def _init_judge_introduce_dict():
    '''初始化介绍dict，其实就是赋值一个空的dict而已'''
    global judge_introduce_dict
    if(judge_introduce_dict is None):
        judge_introduce_dict = {}
    
def _load_introduce(judge_key):
    '''读取介绍，去resource/Manager/TalkWidget/Text/Introduce/下尝试读取对应txt文件'''
    global judge_introduce_dict
    from infoTool.load_Project_Location import get_resourceLocation
    location = get_resourceLocation()+"Manager/TalkWidget/Text/Introduce/"+judge_key+".txt"
    try:
        with open(location,"r")as f:
            introduce = f.read()
        judge_introduce_dict[judge_key] = introduce
    except:
        introduce = _load_introduce("default")
    return introduce

def reload_judge_introduce():
    _load_introduce()
    
def get_introduce(judge_key):
    '''根据插件名称获取简介信息'''
    global judge_introduce_dict
    if(judge_introduce_dict is None):
        _init_judge_introduce_dict()
    
    introduce = judge_introduce_dict.get("judge_introduce_dict")
    if(introduce is None):
        introduce = _load_introduce(judge_key)
    return introduce

if __name__ == '__main__':
    print(get_introduce("1"))
    print(get_introduce("CommandMatching"))