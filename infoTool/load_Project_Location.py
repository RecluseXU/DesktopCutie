# -*- coding: utf-8 -*-
'''
Created on 2019年1月8日

@author: RecluseXu
'''

projectLocation = None

def get_ProjectLocation():
    # 获取项目根路径
    global projectLocation
    if(projectLocation is None):
        print("获取项目路径......")
        import sys
        address = sys.argv[0].replace("\\","/")
        projectLocation = address[:address.find("/DesktopCutie/")+len("/DesktopCutie/")]
        
        print(projectLocation)
        
        return projectLocation
    else:
        return projectLocation

def get_IconFolder_location():
    '''获取图标文件夹路径'''
    return get_resourceLocation()+"Manager/picture/Icon/"

def get_resourceLocation():
    # 获取项目资源路径
    return get_ProjectLocation() + "resource/"

def get_PressKeyMapper_location():
    '''获取热键保存地址'''
    return get_resourceLocation()+"Manager/TalkWidget/PressKeyMapper.json"

def get_TheCuiteFolderLocation(cuiteID):
    # 获取指定Cuite的资源文件夹绝对路径
    return get_resourceLocation() + cuiteID + "/"

def get_auto_reply_location():
    '''获取放置自动回复的路径'''
    return get_resourceLocation()+"Manager/TalkWidget/Judgement/AutoReply/"

def get_judge_model_folder_location():
    '''获取放置判断模型的文件夹位置'''
    return get_resourceLocation()+"Manager/TalkWidget/Judgement/JudgeModel/"

def get_SoftwareMapper_location():
    '''获取软件mapper的路径'''
    return get_resourceLocation() + "Manager/TalkWidget/SoftwareMapper.json"

def get_FairyInfoNote_folder_location():
    '''获取存放精灵简要信息文件夹的路径'''
    return get_resourceLocation() + "Manager/FairySetWidget/FairyInfoNote/"

def get_JudgeStepList_location():
    '''获取判断步骤列表文件的位置'''
    return get_resourceLocation()+"Manager/TalkWidget/Judgement/JudgeStepList.ini"

def get_ManagerConfigure_Location():
    '''获取管理器设置文件路径'''
    return get_resourceLocation() + "Manager/"

if __name__ == '__main__':
    for i in range(2):
        print(get_ProjectLocation())
    print(get_resourceLocation())
