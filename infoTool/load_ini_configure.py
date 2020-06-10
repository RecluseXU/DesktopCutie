# -*- coding: utf-8 -*-
'''
Created on 2019年4月1日

@author: RecluseXu
'''

# 读取ini配置文件
import configparser
from infoTool.load_Project_Location import get_JudgeStepList_location

# 由于configparser存在无论大小写都识别为小写的问题，所以要改一下类
class MyConfigParser(configparser.ConfigParser): 
# --------------------- 
# 作者：Lin-Bo 
# 来源：CSDN 
# 原文：https://blog.csdn.net/Ha_hha/article/details/78965011 
    def __init__(self, defaults=None): 
        configparser.ConfigParser.__init__(self, defaults=defaults) 
    def optionxform(self, optionstr): 
        return optionstr




def _load_ini(ini_location):
    '''
    传入配置文件路径，读取配置文件，返回一个configparser.ConfigParser 对象
    '''
    # 步骤一：
    config = MyConfigParser()
    # 步骤二:读取文件内容
    config.read(ini_location)
    # 步骤三:获取选项值
    return config

def load_ini_value(ini_location, aim_option_list):
    '''
    传入一个[[大项名,小项名],] 。结果将以list对应返回
    '''
    config = _load_ini(ini_location)
    if(config is None):
        return
    
    value_list = []
    for aim_option in aim_option_list:
        value_list.append(config.get(aim_option[0], aim_option[1]))
    return value_list

def set_ini_value(ini_location, aim_option_list):
    '''
    传入一个[[大项名,小项名,值],] 。修改配置对应值,并保存
    '''
    config = _load_ini(ini_location)
    for aim_option in aim_option_list:
        config.set(aim_option[0], aim_option[1], str(aim_option[2]))
    with open(ini_location,"w")as f:
        config.write(f)

def delete_ini_key(ini_location, aim_option_list):
    '''
    传入一个[[大项名,小项名],] 。删除对应项,并保存
    '''
    config = _load_ini(ini_location)
    for aim_option in aim_option_list:
        config.remove_option(aim_option[0], aim_option[1])
    with open(ini_location,"w")as f:
        config.write(f)

def load_ini_element_to_only_list(ini_location, option_name):
    '''
    传入一个大项名，将其中的元素以[[key,value]]的形式返回
    '''
    config = _load_ini(ini_location)
    return list(map(lambda x:list(x), config.items(option_name)))

def load_ini_element_to_set_list(ini_location, option_name):
    '''
    传入一个大项名，将其中的元素以[(key,value)]的形式返回
    '''
    config = _load_ini(ini_location)
    return config.items(option_name)

def recreat_ini(ini_location, option_name_list, element_aim_list):
    '''
    重建ini，清除所有东西，再次建立项目
    传入需要建立的大项列表，元素设置列表[[大项名称，小项名，值]]
    '''
    config = _load_ini(ini_location)
    config.clear()
    for option_name in option_name_list:
        config.add_section(option_name)
    for element in element_aim_list:
        config.set(element[0], element[1], element[2])
    with open(ini_location,"w")as f:
        config.write(f)


if __name__  == "__main__":
#     location = "D:/github_repository/DesktopFairy/DesktopCutie/resource/Manager/ManagerConfigure.ini"
#     aim_list = [["TalkFrame","Auto_Creat"],["FairyFrame","Auto_Creat"]]
#     a = load_ini_value(location, aim_list)
    
#     set_ini_value(location, [["FairyFrame","111",1]])
#
#     location = get_JudgeStepList_location()
#     delete_ini_key(location, [["","text"]])

#     location = get_JudgeStepList_location()
#     print(load_ini_element_to_only_list(location,"JudgeStepList"))
    print(load_ini_element_to_only_list(get_JudgeStepList_location(),"JudgeStepList"))