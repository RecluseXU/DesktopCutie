# -*- coding: utf-8 -*-
'''
Created on 2019年3月6日

@author: RecluseXu
'''
from PyQt5.QtGui import QIcon

icon_dict = None

def _load_all_icon():
    global icon_dict
    
    from infoTool.load_Project_Location import get_resourceLocation
    from infoTool.scan_file import scan_file
    print("读取图标......")
    location = get_resourceLocation()+"Manager/picture/Icon/"
    icon_dict = scan_file(location, "")
    print(icon_dict)
    
def reload_icon():
    '''
    重载所有图标
    认为    resource/Manager/picture 目录下所有文件都是图标
    扫描完后，文件名作为 key,文件路径作为value。
    在需要用时，才替换为QIcon，这样或许能节约内存空间？？？？
    '''
    _load_all_icon()
    
def get_icon_by_key(key):
    '''
    传入图标文件名（不带拓展名），获取图标（QIcon）。
    '''
    
    global icon_dict
    
    # 尚未初始化时，先初始化 
    # 实现如同单例那样的效果
    if(icon_dict is None):
        _load_all_icon()
    
    # 初始化完成后，里面保存的是图片路径而不是图标。
    # 当想要获取图标时，先用图标代替icon_dict中的路径字符，再返回图标
    the_icon = icon_dict.get(key)
    if(isinstance(the_icon, str)):
        icon_dict[key] = QIcon(the_icon)
    return icon_dict.get(key)

if __name__ == '__main__':
    print(get_icon_by_key("1"))
    print(get_icon_by_key("set"))
    print(get_icon_by_key("set"))