# -*- coding: utf-8 -*-

'''
Created on 2019年2月19日10:26:07

@author: RecluseXU
'''

from model.performers.judge_resoult_performers import add_performent
from model.reply.reply import add_auto_reply
from model.CLASS.JudgeResoult import JudgeResoult

from model.judge import _JudgeStepList_helper as JudgeStepList, JudgeModel_helper as JudgeModel

#-----------------------------------------------------------
# 判断步骤列表相关
def get_judge_step_list():
    return JudgeStepList._get_judge_step_list()
def enable_judge_step(judge_name):
    JudgeStepList._enable_judge_step(judge_name)
def disable_judge_step(judge_name):
    JudgeStepList._disable_judge_step(judge_name)
def save_judge_step():
    JudgeStepList._save_judge_step()
def reload_judgement_list():
    JudgeStepList._reload_judgement_list()
def move_up_a_judge_step(judge_step_name):
    JudgeStepList._move_up_a_judge_step(judge_step_name)
def move_down_a_judge_step(judge_step_name):
    JudgeStepList._move_down_a_judge_step(judge_step_name)
def delete_judge_step(judge_name):
    JudgeStepList._delete_judge_step(judge_name)
def add_judge_step(judge_step_name):
    JudgeStepList._add_judge_step(judge_step_name)

#-----------------------------------------------------------
# 判断模型相关
def delete_judge_model(judge_name):
    JudgeModel.delete_judge_model(judge_name)
def get_a_judgement(judge_name):
    return JudgeModel.get_a_judge_model(judge_name)
def get_judgement_dict():
    return JudgeModel.get_judgement_dict()

#-----------------------------------------------------------

def check_add_new_model_to_judge_step_list():
    # 检查一下，看看判断顺序表里的东西有没有比检查到的判断函数少
    # 如果少了，说明有新的判断函数被添加，那么就将他加入判断顺序表
    py_dict = JudgeModel.get_judgement_dict()
    judge_step_list = JudgeStepList._get_judge_step_list()
    
    if(len(judge_step_list) < len(py_dict.keys())):
        # 将现在的步骤列表中的步骤与模块列表的步骤做交集
        now_step_name_list = map(lambda x:x[0], judge_step_list)
        model_name_list = list(py_dict.keys())
        need_add_list = list(set(now_step_name_list)^set(model_name_list))
        
        for new_judge_name in need_add_list:
            add_judge_step(new_judge_name)

def delete_a_judgement(judge_name):
    '''
    删除一个插件
    '''
    print("删除模组",judge_name)
    # 删除判断列表对应项
    delete_judge_step(judge_name)
    # 删除插件模组项
    delete_judge_model(judge_name)

def judge_process(input_str):
    '''
    判断
    '''
    # 加载判断插件判断顺序与启用配置
    judge_step_list = get_judge_step_list()
    
    # 加载判断插件实际判断函数
    judge_model_dict = get_judgement_dict()
    
    
    for judgement in judge_step_list:
#         print(judgement)
        if(judgement[1] == '0'):
            continue
        
        # 将判断函数拿出来，传入输入。
        judge_resoult = judge_model_dict[judgement[0]].judge(input_str)
        
        # 当返回的结果不是字符串，意味着已经判断成功，那么直接退出去
        if(isinstance(judge_resoult, str) == False):
            break
            
    if(isinstance(judge_resoult, str) == True):
        return JudgeResoult(input_str, False)
    
    judge_resoult = add_performent(judge_resoult)
    judge_resoult = add_auto_reply(judge_resoult)
    return judge_resoult


    
if __name__=="__main__":
    re = judge_process("./qq")
    re = judge_process("hi")
    print(re.is_succeed)
    print(re.operation_str)
    print(re.perform())
    
    get_judge_step_list()
    get_judgement_dict()
