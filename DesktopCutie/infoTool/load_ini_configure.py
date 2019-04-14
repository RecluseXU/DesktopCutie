# -*- coding: utf-8 -*-
'''
Created on 2019年4月1日

@author: RecluseXu
'''

# 读取ini配置文件
import configparser

def _load_ini(ini_location):
    '''
    传入配置文件路径，读取配置文件，返回一个configparser.ConfigParser 对象
    '''
    # 步骤一：
    config = configparser.ConfigParser()
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

if __name__  == "__main__":
    location = "D:/github_repository/DesktopFairy/DesktopCutie/resource/Manager/ManagerConfigure.ini"
    aim_list = [["TalkFrame","Auto_Creat"],["FairyFrame","Auto_Creat"]]
    a = load_ini_value(location, aim_list)
    set_ini_value(location, [["TalkFrame","Auto_Creat",1]])
    print(a)