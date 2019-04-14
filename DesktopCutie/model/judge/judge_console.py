# -*- coding: utf-8 -*-

'''
Created on 2019年2月19日10:26:07

@author: RecluseXU
'''

from infoTool.load_Project_Location import get_judge_model_folder_location, get_JudgeStepList_location
from model.performers.judge_resoult_performers import add_performent
from model.reply.reply import add_auto_reply
from model.CLASS.JudgeResoult import JudgeResoult


judge_step_list = None


def _load_judgement_list():
    '''
    获取判断列表
    '''
    global judge_step_list
    
    judge_step_list = []
    judgement_step_list_location = get_JudgeStepList_location()
    with open(judgement_step_list_location,"r")as f:
        judge_step_list_str = f.read().split("\n")
    
    for judgement in judge_step_list_str:
        judge_step_list.append(judgement.split("="))
        
    print('获取判断步骤列表......\n',judge_step_list)

def reload_judgement_list():
    '''
    重新加载判断列表
    '''
    _load_judgement_list()


def move_down_a_judge_step(judge_step_name):
    '''
    将一个判断步骤后移，当已经在最后时，不会有反应
    '''
    global judge_step_list
    i = len(judge_step_list)-1
    while(i > 0):
        if(judge_step_list[i-1][0] == judge_step_name):
            # 交换位置
            judge_step_list[i-1], judge_step_list[i] = judge_step_list[i], judge_step_list[i-1]
        i = i-1

def move_up_a_judge_step(judge_step_name):
    '''
    将一个判断步骤前移，当已经在最前时，不会有反应
    '''
    global judge_step_list
    i = 1
    while(i < len(judge_step_list)):
        if(judge_step_list[i][0] == judge_step_name):
            # 交换位置
            judge_step_list[i-1], judge_step_list[i] = judge_step_list[i], judge_step_list[i-1]
        i = i+1

def get_judge_step_list():
    '''
    获取判断步骤列表(list)
    '''
    # 加载判断插件判断顺序与启用配置
    global judge_step_list
    if(judge_step_list is None):
        _load_judgement_list()
    
    # 加载判断插件实际判断函数
    global judge_model_dict
    if(judge_model_dict is None):
        _scan_py_judgement()
    
    return judge_step_list

def get_judgement_dict():
    '''
    获取判断插件表(dict)
    '''
    
    # 加载判断插件实际判断函数
    global judge_model_dict
    if(judge_model_dict is None):
        _scan_py_judgement()
    
    return judge_model_dict

def get_a_judgement(judge_name):
    '''
    获取判断插件表(dict)
    '''
    
    # 加载判断插件实际判断函数
    global judge_model_dict
    if(judge_model_dict is None):
        _scan_py_judgement()
    
    return judge_model_dict.get(judge_name)
    
def enable_judge_step(judge_name):
    '''
    启动一个判断列表中的判断
    修改完毕后会保存设置到设置文件中去
    '''
    global judge_step_list
    for judge_step in judge_step_list:
        # 未启动，且与目标一致
        if(judge_step[1]=='0' and judge_name == judge_step[0]): 
            judge_step[1]='1'
    save_judge_step()
    
def disable_judge_step(judge_name):
    '''
    禁用一个判断列表中的判断
    修改完毕后会保存设置到设置文件中去
    '''
    global judge_step_list
    for judge_step in judge_step_list:
        # 已经启动，且与目标一致
        if(judge_step[1] == '1' and judge_name == judge_step[0]): 
            judge_step[1]='0'
    save_judge_step()
    

def save_judge_step():
    '''
    保存当前判断步骤状态到文件中
    '''
    global judge_step_list
    a = ""
    for judge_step in judge_step_list:
        a = a + judge_step[0]+"="+judge_step[1]+"\n"
    a = a[:-1]
    
    location = get_JudgeStepList_location()
    with open(location,"w")as f:
        f.write(a)


judge_model_dict = None
def _scan_py_judgement():
    '''
    扫描判断目录，将里面的含有judge函数文件认为是判断源文件
    返回一个dict，格式:{ "文件名" : 里面的judge函数 }
    '''
    # 获取、计算判断目录
    location = get_judge_model_folder_location()
         
    # 扫描判断模型目录下所有.py文件
    from infoTool.scan_file import scan_file
    py_dict = scan_file(location, file_type="py")
    print("!!!",py_dict)
    
    # 获取到对应的判断函数，保存起来
    from infoTool.importer import get_python_model_or_function
    for judge_name in list(py_dict.keys()):
        py_dict[judge_name] = get_python_model_or_function(location, judge_name, "judge")
    global judge_model_dict
    judge_model_dict = py_dict
    
    # 检查一下，看看判断顺序表里的东西有没有比检查到的判断函数少
    # 如果少了，说明有新的判断函数被添加，那么就将他加入判断顺序表
    global judge_step_list
    if(len(judge_step_list) < len(py_dict.keys())):
        a=[]
        for x in judge_step_list:
            a.append(x[0])
        b = list(py_dict.keys())
        
        need_add_list = list(set(a)^set(b))
        
        a=[]
        for i in need_add_list:
            a.append([i, "0"])
        judge_step_list.extend(a)
        # 保存判断步骤
        save_judge_step()
        
        
def judge_process(input_str):
    '''
    判断
    '''
    # 加载判断插件判断顺序与启用配置
    global judge_step_list
    if(judge_step_list is None):
        _load_judgement_list()
    
#     print(judge_step_list)
    
    # 加载判断插件实际判断函数
    global judge_model_dict
    if(judge_model_dict is None):
        _scan_py_judgement()
    
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

