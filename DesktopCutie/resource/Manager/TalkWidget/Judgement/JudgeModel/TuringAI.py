#!/user/bin/env python3
#!-*- coding:utf-8 -*-
'''
Created on 2018年5月27日12:41:13

@author: RecluseXU
'''
# -*- coding: utf-8 -*-
'''
Created on 2019年3月7日

@author: RecluseXu
'''
import requests
import json

turing_user_info_dict = None

def _load_turing_userdata():
    '''
    读取用户接入数据
    '''
    global turing_user_info_dict
    
    from infoTool.load_Project_Location import get_resourceLocation
    location = get_resourceLocation()+"Manager/TalkWidget/Judgement/TuringAI.json"
    
    with open(location, "r")as f:
        turing_user_info_dict = json.load(f)

def _chat(input_str): #和秋叶聊天
    #print(address)
    
    global turing_user_info_dict
    if(turing_user_info_dict is None):
        _load_turing_userdata()
    
    data = {
        "reqType":0, #输入类型:0-文本(默认)、1-图片、2-音频
        "perception":{
            "inputText": {
                "text": input_str
                },
            "selfInfo": {
                "location": {
                    "city": "",
                    "province": "",
                    }
                }
            },
        "userInfo":{
            "apiKey": turing_user_info_dict["apiKey"],
            "userId": turing_user_info_dict["userId"]
            }
        }

    r = requests.post("http://openapi.tuling123.com/openapi/api/v2", data = json.dumps(data))
    k = r.json().get("results")
    r.close()
    
    reply = k[0].get("values").get("text")
    if(len(k)>=2):
        print('情况不明', k[1])
    #print(command_dict["result"])
    #print(command_dict["reply"])
    return reply

def reload_turing_userdata():
    '''重新读入用户配置数据'''
    _load_turing_userdata()




#----------------------------------------------


def judge(input_str):
    from model.CLASS.JudgeResoult import JudgeResoult
    judge_resoult = JudgeResoult(input_str,True)
    judge_resoult.operation_str = "ChatTuring"
    judge_resoult.parameter = input_str
    judge_resoult.judge_type = "Turing"
    judge_resoult.reply = _chat(input_str)
    
    return judge_resoult


