# -*- coding: utf-8 -*-

'''
Created on 2019年3月7日

@author: RecluseXu
'''
import json
import random
from infoTool.load_Project_Location import get_auto_reply_location

def load_reply_from_local_file(operation_str):
    '''
    读取自动回复文件，在自动回复文件中选一个回复(str)来返回
    '''
    loaction = get_auto_reply_location()+operation_str+".json"
    print(loaction)
    try:
        with open(loaction,"r")as f:
            replydict = json.load(f)
        select_num = random.randint(1,len(replydict))
        return replydict[str(select_num)]
    except:
        print("读取本地回复失败")
        return None

def add_auto_reply(JudgeResoult):
    '''
    对于没有在模型中设置回复的，看看有没有在文件夹中设置回复，有就加上
    '''
    if(JudgeResoult.is_succeed == False):
        return JudgeResoult
    if(JudgeResoult.reply is not None):
        return JudgeResoult
    
    # 有些操作在本地存有回复信息，尝试获取。
    local_reply = load_reply_from_local_file(JudgeResoult.operation_str)
    
    replace_thing, pro, wr = get_replace_thing(local_reply)
    if(replace_thing is not None):
        for parameter in list(JudgeResoult.perform_parameter.keys()):
            if(parameter == replace_thing):
                true_reply =  pro + JudgeResoult.perform_parameter[parameter] + wr
        JudgeResoult.reply = true_reply
    else:
        JudgeResoult.reply = local_reply
    return JudgeResoult

def get_replace_thing(local_reply):
    shape_char1 = local_reply.find("#")
    shape_char2 = local_reply.find("#",shape_char1+1)
    replace_thing_no_shape = local_reply[shape_char1+1:shape_char2]
    pro = local_reply[:shape_char1]
    wr = local_reply[shape_char2+1:]
    if(shape_char1!=-1 and shape_char2!=-1 and len(replace_thing_no_shape)>0):
        return replace_thing_no_shape, pro, wr
    return None,None,None



if(__name__ == "__main__"):
    local_reply = load_reply_from_local_file("OpenSoftwareOrFolder")
    print(local_reply)
    shape_char1 = local_reply.find("#")
    shape_char2 = local_reply.find("#",shape_char1+1)
    
    replace_thing_no_shape = local_reply[shape_char1+1:shape_char2]
    pro = local_reply[:shape_char1]
    wre = local_reply[shape_char2+1:]
    
    
    print(pro,wre)

