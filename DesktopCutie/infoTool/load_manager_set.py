# -*- coding: utf-8 -*-

'''
Created on 2019年4月10日

@author: RecluseXu
'''
from infoTool.load_ini_configure import load_ini_value, set_ini_value
from infoTool.load_Project_Location import get_ManagerConfigure_Location

def get_manager_auto_start_configure():
    '''
    获取自启动设置 ,返回{"TalkFrame":boolean, "FairyFrame":fairyID（str）/None}  
    '''
    location = get_ManagerConfigure_Location()+"ManagerConfigure.ini"
    auto_start_list = load_ini_value(location, [["TalkFrame", "auto_creat"],["FairyFrame","auto_creat"]])
    if(auto_start_list[0]=="1"):
        auto_start_list[0] = True
    else:
        auto_start_list[0] = False
    
    if(auto_start_list[1]=="None"):
        auto_start_list[1] = None
    
    return {"TalkFrame":auto_start_list[0], "FairyFrame":auto_start_list[1]}

def set_talkframe_auto_start_configure(is_auto_start):
    '''
    设置对话框自启动，传入True或False(boolean)
    '''
    
    #将boolean转化为字符一些字符，才能保存，这里我转化为1或0
    if(is_auto_start):
        con_str = "1"
    else:
        con_str = "0"
    location = get_ManagerConfigure_Location()+"ManagerConfigure.ini"
    set_ini_value(location, [["TalkFrame", "auto_creat" , con_str]])

def set_fairyframe_auto_start_configure(fairy_id):
    '''
    设置精灵界面自启动，传入精灵id或者None
    '''
    location = get_ManagerConfigure_Location()+"ManagerConfigure.ini"
    if(fairy_id is None):
        fairy_id = "None"
    
    set_ini_value(location, [["FairyFrame", "auto_creat" , fairy_id]])

if __name__ == "__main__":
    print(get_manager_auto_start_configure())