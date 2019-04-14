# -*- coding: utf-8 -*-

'''
Created on 2019年3月12日

@author: RecluseXu
'''

import importlib
from infoTool.load_Project_Location import get_ProjectLocation
import sys
import imp
def get_python_model_or_function(location, model_name, function_name=None): 
    '''
    传入路径与python源文件名(末位不用带.py)，获取目标模块。
    如果传入一个函数名，那么会判断该源是否有 传入函数名的函数，如果没有，就会返回None
    '''
    
    # TYPE1
    # 将地址转换为 相对于项目而言的包的形式，再加上模块名
    # D:/github_repository/DesktopFairy/DesktopCutie/Manager/TalkWidget/Judgement/JudgeModel/
    # To
    # resource.Manager.TalkWidget.Judgement.JudgeModel
#     location = location.replace(get_ProjectLocation(),"").replace("/",".")+model_name
#     the_model = importlib.import_module(location)  # 根据location，导入模块
    
    # TYPE2
    the_model = imp.load_source(model_name, location+model_name+".py")
    
    if(function_name is not None):
        # 如果模块没有指定函数名的函数
        if(hasattr(the_model, function_name) == False):
            return None
     
    if(the_model is not None):
        return the_model
    


if __name__=="__main__":
    from infoTool.load_Project_Location import get_judge_model_folder_location
    location = get_judge_model_folder_location()
    print(get_python_model_or_function(location, "TuringAI" ,function_name="judge"))