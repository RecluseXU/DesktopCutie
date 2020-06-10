# -*- coding: utf-8 -*-
'''
Created on 2019年2月16日

@author: RecluseXu
'''
import os


def scan_file(location, file_type=""):
    '''
    传入想要扫描的文件夹路径 与 文件扩展名（后缀，点后面那几个字母, 不包括那个点）返回扫描到的文件。  
    '''
    xmlDict = {}
    path = location
#     print("扫描"+path+"目录下所有"+file_type+"文件......")
    f_list = os.listdir(path)
    for i in f_list:
        #  有拓展名的，是一个文件
        k = i.find(".")
        if(k != -1):
            if(file_type == ""):  # 如果传入的类型什么也没有
                xmlDict[i[:k]] = path + i
            elif(os.path.splitext(i)[1] == '.'+file_type):  # 如果传入了类型
                # os.path.splitext():分离文件名与扩展名
                xmlDict[i[:k]] = path + i
    return xmlDict


if __name__ == '__main__':
    from infoTool.load_Project_Location import get_resourceLocation
    location = get_resourceLocation()+"Manager/picture/Icon"
    print(location)
    print(scan_file(location, ""))
    print(scan_file(location, "png"))
    print(scan_file("/", ""))
