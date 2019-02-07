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
        return projectLocation
    else:
        return projectLocation

def get_resourceLocation():
    # 获取项目资源路径
    return get_ProjectLocation() + "resource/"

def get_TheCuiteFolderLocation(cuiteID):
    # 获取指定Cuite的资源文件夹绝对路径
    return get_resourceLocation() + cuiteID + "/"
    

if __name__ == '__main__':
    for i in range(2):
        print(get_ProjectLocation())
    print(get_resourceLocation())
