# -*- coding: utf-8 -*-
'''
Created on 2019年4月15日

@author: RecluseXu
'''

from infoTool.load_Project_Location import get_judge_model_folder_location
from infoTool.scan_file import scan_file
from infoTool.importer import get_python_model_or_function
import os

judge_model_dict = None

def load_judge_model():
    # 加载判断插件实际判断函数
    global judge_model_dict
    if(judge_model_dict is None):
        _scan_py_judgement()
        
def get_judgement_dict():
    '''
    获取判断插件表(dict)
    '''
    
    # 加载判断插件实际判断函数
    global judge_model_dict
    if(judge_model_dict is None):
        _scan_py_judgement()
    
    return judge_model_dict

def get_a_judge_model(judge_name):
    '''
    获取判断插件表(dict)
    '''
    # 加载判断插件实际判断函数
    global judge_model_dict
    if(judge_model_dict is None):
        _scan_py_judgement()
    
    return judge_model_dict.get(judge_name)

def delete_judge_model(judge_name):
    '''
    删除一个判断模组
    '''
    file_location = get_judge_model_folder_location()+judge_name+".py"
    # 如果文件存在才删除
    if(os.path.exists(file_location)):
        os.remove(file_location)
    else:
        print("欲删除的插件模型文件"+file_location+"不存在")

def _scan_py_judgement():
    '''
    扫描判断目录，将里面的含有judge函数文件认为是判断源文件
    返回一个dict，格式:{ "文件名" : 里面的judge函数 }
    '''
    global judge_model_dict
    print("扫描插件模组......")
    # 获取、计算判断目录
    location = get_judge_model_folder_location()
    
    # 扫描判断模型目录下所有.py文件
    py_dict = scan_file(location, file_type="py")
    
    # 获取到对应的判断函数，保存起来
    for judge_name in list(py_dict.keys()):
        py_dict[judge_name] = get_python_model_or_function(location, judge_name, "judge")
    judge_model_dict = py_dict
    print(judge_model_dict)

    