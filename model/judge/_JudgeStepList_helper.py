# -*- coding: utf-8 -*-
'''
Created on 2019年4月15日

@author: RecluseXu
''' 
from infoTool.load_Project_Location import get_JudgeStepList_location
from infoTool.load_ini_configure import load_ini_element_to_only_list,delete_ini_key, recreat_ini


judge_step_list = None

def _load_judgement_list():
    '''
    获取判断列表
    '''
    global judge_step_list
    judge_step_list = load_ini_element_to_only_list(get_JudgeStepList_location(),"JudgeStepList")
    
    print('获取判断步骤列表......\n',judge_step_list)

def _reload_judgement_list():
    '''
    重新加载判断列表
    '''
    _load_judgement_list()

def _add_judge_step(judge_step_name):
    '''
    添加新的模块名称进判断列表
    '''
    global judge_step_list
    
#     判断传入的判断步骤是否已经在列表中
#     if(judge_step_name in list(map(lambda x:x[0], judge_step_list))):
#         return
    judge_step_list.extend([[judge_step_name, '0']])
    # 保存判断步骤
    _save_judge_step()

def _move_down_a_judge_step(judge_step_name):
    '''
    将一个判断步骤后移，当已经在最后时，不会有反应
    '''
    global judge_step_list
    print("插件后移", judge_step_name)
    i = len(judge_step_list)-1
    while(i > 0):
        if(judge_step_list[i-1][0] == judge_step_name):
            # 交换位置
            judge_step_list[i-1], judge_step_list[i] = judge_step_list[i], judge_step_list[i-1]
        i = i-1
    _save_judge_step()

def _move_up_a_judge_step(judge_step_name):
    '''
    将一个判断步骤前移，当已经在最前时，不会有反应
    '''
    global judge_step_list
    print("插件前移",judge_step_name)
    i = 1
    while(i < len(judge_step_list)):
        if(judge_step_list[i][0] == judge_step_name):
            # 交换位置
            judge_step_list[i-1], judge_step_list[i] = judge_step_list[i], judge_step_list[i-1]
        i = i+1
    _save_judge_step()
    
def _enable_judge_step(judge_name):
    '''
    启动一个判断列表中的判断
    修改完毕后会保存设置到设置文件中去
    '''
    global judge_step_list
    for judge_step in judge_step_list:
        # 未启动，且与目标一致
        if(judge_step[1]=='0' and judge_name == judge_step[0]): 
            judge_step[1]='1'
    _save_judge_step()
    
def _disable_judge_step(judge_name):
    '''
    禁用一个判断列表中的判断
    修改完毕后会保存设置到设置文件中去
    '''
    global judge_step_list
    for judge_step in judge_step_list:
        # 已经启动，且与目标一致
        if(judge_step[1] == '1' and judge_name == judge_step[0]): 
            judge_step[1]='0'
    _save_judge_step()

def _save_judge_step():
    '''
    保存当前判断步骤启用状态到文件中
    '''
    global judge_step_list
    save_list = []
    for judge_step in judge_step_list:
        save_list.append(["JudgeStepList", judge_step[0], judge_step[1]])
    recreat_ini(get_JudgeStepList_location(),["JudgeStepList"], save_list)


def _delete_judge_step(judge_name):
    '''
    删除判断步骤
    '''
    global judge_step_list
    
#     new_list = []
#     for judge_step in judge_step_list:
#         if(judge_step[0] != judge_name):
#             new_list.append(judge_step)
#     judge_step_list = new_list
    
    delete_ini_key(get_JudgeStepList_location(), [["JudgeStepList",judge_name]])
    _reload_judgement_list()
    _save_judge_step()

def _get_judge_step_list():
    '''
    获取判断步骤列表(list)
    '''
    global judge_step_list
    if(judge_step_list is None):
        # 尚未加载，则加载
        _load_judgement_list()
        check_model_change()
    
    return judge_step_list

def check_model_change():
    # 检查一下，看看判断顺序表里的东西有没有比检查到的判断函数少
    # 如果少了，说明有新的判断函数被添加，那么就将他加入判断顺序表
    from model.judge.judge_console import get_judgement_dict
    
    global judge_step_list
    py_dict = get_judgement_dict()
    
    if(len(judge_step_list) < len(py_dict.keys())):
        # 将现在的步骤列表中的步骤与模块列表的步骤做交集
        now_step_name_list = map(lambda x:x[0], judge_step_list)
        model_name_list = list(py_dict.keys())
        need_add_list = list(set(now_step_name_list)^set(model_name_list))
        
        for new_judge_name in need_add_list:
            _add_judge_step(new_judge_name)


if __name__=="__main__":
    pass